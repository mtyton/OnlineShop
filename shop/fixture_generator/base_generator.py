from django.core.management import call_command


class BaseGenerator(object):
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

    def __init__(self, fill_data=False, no_validate=False):
        # TODO - make usage of no validate option
        pass

    def __fill_model_with_data(self) -> bool:
        # TODO - there should be implemented mechanism which will allow to
        # fills data with some dummy data
        return False

    def __delete_created_records(self) -> bool:
        return False

    def run(self) -> None:
        # There has to be fixtures map defined
        assert len(self.fixtures_map.keys()) != 0

        for fixture_name, models in self.fixtures_map.items():
            # TODO add fixture name validation
            call_command('dumpdata', models, **{'output': fixture_name})
