import os

from typing import List
from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--apps', nargs='+',
            help='List of applications names for which '
                 'fixtures will be generated'
        )

    def __discover_generators(self, apps: List[str]) -> List[str]:
        # TODO add applications_names
        exec(
            f"from {settings.FIXTURE_GENERATOR_PATH} "
            f"import {settings.FIXTURE_GENERATOR_DISCOVERER}"
        )
        discoverer = eval(settings.FIXTURE_GENERATOR_DISCOVERER)()
        return discoverer.get_generators(apps)

    def __create_and_run_generators(self, apps: List[str]):
        generators_paths = self.__discover_generators(apps)
        for generator_path in generators_paths:
            generator_name = generator_path.replace('.', '_')
            exec(
                f"from {generator_path} "
                f"import {settings.FIXTURE_GENERATOR_CLASS_NAME} "
                f"as {generator_name}"
            )
            generator = eval(generator_name)()
            generator.run()

    def handle(self, *args, **kwargs):
        apps = kwargs.get('apps', [])
        self.__create_and_run_generators(apps)
