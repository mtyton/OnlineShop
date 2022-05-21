import os
import sys

from django.conf import settings
from django.core.management import call_command

# from fixture_generator.data_generators import StandardDataGenerator


# TODO - fix this class
class BaseGenerator:
    """
    This class is the base fixture generator
    for creating test-fixtures
    """

    """
    This is the map of fixtures, this should look like this:
    'fixture_name': List[model_names]
    You should provide model_name like this: app_name.model_name
    Eg:
    {'test_full_users': ['auth.User', 'auth.Groups']}
    """
    fixtures_map = {}

    def __init__(self, data_generator_class=None, fill_data=False):
        self.data_generator = None  # data_generator_class()
        self.fill_data = fill_data

    # def __fill_model_with_data(self) -> bool:
    #     # TODO - there should be implemented mechanism which will allow to
    #     # fills data with some dummy data
    #     return False
    #
    # def __delete_created_records(self) -> bool:
    #     return False

    def __build_fixture_path(self, fixture_name: str) -> str:
        base_path = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
        return f"{base_path}/" f"{settings.DEFAULT_FIXTURE_GENERATOR_DIRECTORY_NAME}/" f"{fixture_name}"

    def run(self) -> None:
        # There has to be fixtures map defined
        assert len(self.fixtures_map.keys()) != 0

        for fixture_name, models in self.fixtures_map.items():
            fixture_path = self.__build_fixture_path(fixture_name)
            # TODO add fixture name validation
            call_command("dumpdata", models, **{"output": fixture_path})
