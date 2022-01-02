from fixture_generator.base_generator import BaseGenerator


# This is just the test generator, which should not be discovered
class Generator(BaseGenerator):
    # For test purposes, use django base models
    fixtures_map = {
        'test_full_generators': ['auth.User', 'auth.Group']
    }
