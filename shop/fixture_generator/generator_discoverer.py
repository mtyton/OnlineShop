import os

from typing import Protocol, List
from django.conf import settings
from django.apps import apps


class BaseGeneratorDiscoverer(Protocol):
    def _discover_local_django_apps(self):
        ...

    def _discover_generators(self):
        ...

    def _verify_import(self):
        ...

    def get_generators(self, apps_names: List[str]):
        ...


class StandardGeneratorDiscoverer:
    def __init__(self, root_directory=settings.BASE_DIR):
        self.root_directory = root_directory

    def _discover_local_django_apps(self, apps_names: List[str]) -> List[str]:
        """
        This method discovers which of INSTALLED_APPS are really the local
        django apps. In case there are given applications in the command this
        method won't bother searching all application,
        it'll simply search only in applications given.
        """
        if not apps_names:
            applications = [
                app.verbose_name.lower() for app in apps.get_app_configs()
            ]
        else:
            applications = apps_names

        dirs = os.listdir(self.root_directory)
        local_applications = [value for value in applications if value in dirs]
        return local_applications

    def _discover_generators(self, apps_names: List[str]) -> List[str]:
        """
        This method returns a list of available import paths for generators.
        If there exists local application with file generator.py inside
        this method will include it in a list.
        """
        local_applications = self._discover_local_django_apps(apps_names)
        generator_import_paths = []
        for application in local_applications:
            search_path = os.path.join(self.root_directory, application)
            if "generator.py" in os.listdir(search_path):
                generator_import_paths.append(f"{application}.generator")
        return generator_import_paths

    def _verify_import(self, available_generators: List[str]) -> List[str]:
        validated_generators = []
        for generator in available_generators:
            try:
                generator_name = f"{generator.split('.')[0]}_generator"
                # TODO - allow using different class names
                path = f"from {generator} import Generator as {generator_name}"
                exec(path)
            except ImportError:
                # TODO - change this to logging to file
                print(f"Unable to import generator from {generator}")
            else:
                validated_generators.append(generator)
        return validated_generators

    def get_generators(self, apps_names: List[str] = None) -> List[str]:
        """
        This method should discover generators for given apps
        (if not given checks for all). It returns a list of dot paths for
        those generators, Eg: app1.generator
        """
        if not apps_names:
            apps_names = []

        available_generators = self._discover_generators(apps_names)
        validated_generators = self._verify_import(available_generators)
        return validated_generators
