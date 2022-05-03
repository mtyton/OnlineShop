import os
import shutil

from django.test import TestCase, override_settings
from django.conf import settings
from django.apps import apps


FIXTURE_TEST_APPS = [
        'fixtureTestApp1', 'fixtureTestApp2', 'fixtureTestApp3'
]


class BaseFixtureGeneratorTestCase(TestCase):

    def _add_generator_to_app(self, app_name: str) -> None:
        """
        Add generator.py file into the application.
        returns True if creating generator was successful,
        otherwise it returns False
        """
        app_path = os.path.join(self.test_directory, app_name)

        template_directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'commons/template_generator.py'
        )
        shutil.copy(
            template_directory,
            os.path.join(app_path, 'generator.py')
        )

    def _remove_generator_from_app(self, app_name: str) -> None:
        """
        Removes generator.py file from the application.
        returns True if deleting generator was successful,
        otherwise it returns False
        """
        app_path = os.path.join(self.test_directory, app_name)
        os.remove(os.path.join(app_path, 'generator.py'))

    def __initialize_single_app(self, app: str) -> None:
        app_path = os.path.join(self.test_directory, app)
        try:
            os.mkdir(app_path)
        except FileExistsError:
            # if not just copy generator and finish
            self._add_generator_to_app(app)
            return

        self._add_generator_to_app(app)
        # use context manager to create __init__.py files
        with open(os.path.join(app_path, '__init__.py'), "w") as f:
            pass

    def _clear_generator(self, app_name: str) -> None:
        """
        This method removes Generator class from generator.py of given app.
        This may be necessary during testing generator imports.
        """
        app_path = os.path.join(self.test_directory, app_name)
        with open(os.path.join(app_path, 'generator.py'), "w") as f:
            # write this to overwrite anything
            f.write(" ")

    def __initialize_apps(self) -> None:
        for app in FIXTURE_TEST_APPS:
            self.__initialize_single_app(app)

    def __remove_apps(self) -> None:
        for app in FIXTURE_TEST_APPS:
            app_path = os.path.join(self.test_directory, app)
            shutil.rmtree(app_path, ignore_errors=False, onerror=None)

    def setUp(self) -> None:
        super().setUp()
        self.test_directory = settings.BASE_DIR
        self.__initialize_apps()
        settings.INSTALLED_APPS = list(apps.get_app_configs()) + FIXTURE_TEST_APPS

    def tearDown(self) -> None:
        super().tearDown()
        self.__remove_apps()
