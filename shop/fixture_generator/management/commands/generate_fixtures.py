import os

from typing import List
from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    GENERATOR_FILENAME = settings.FIXTURE_GENERATOR_FILE_NAME or "generator.py"

    def __discover_generators(self) -> List[str]:
        discoverer_class = exec(f"import {settings.FIXTURE_GENERATOR_DISCOVERER}")
        discoverer = discoverer_class()
        print(discoverer)

    def __create_and_run_generator(self):
        pass

    def handle(self, *args, **kwargs):
        print(self.__discover_generators())
