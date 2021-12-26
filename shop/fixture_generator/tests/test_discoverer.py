from fixture_generator.tests.base import (
    BaseFixtureGeneratorTestCase, FIXTURE_TEST_APPS
)
from fixture_generator.generator_discoverer import StandardGeneratorDiscoverer


class StandardGeneratorDiscovererTestCase(BaseFixtureGeneratorTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.discoverer = StandardGeneratorDiscoverer()

    def test_get_generators_single_app_success(self):
        generators = self.discoverer.get_generators(['fixtureTestApp1'])
        self.assertEqual(generators[0], "fixtureTestApp1.generator")

    def test_get_generators_single_app_no_generators(self):
        self._remove_generator_from_app('fixtureTestApp1')
        generators = self.discoverer.get_generators(['fixtureTestApp1'])
        self.assertEqual(len(generators), 0)

    def test_get_generators_single_app_no_proper_class_defined(self):
        # TODO - there should be file cleaning not removing file
        self._remove_generator_from_app("fixtureTestApp1")
        # in this case there is no Generator class defined in the file
        # so file is not included in the imports
        generators = self.discoverer.get_generators(['fixtureTestApp1'])
        self.assertEqual(len(generators), 0)

    def test_get_generators_all_apps_success(self):
        generators = self.discoverer.get_generators(FIXTURE_TEST_APPS)
        self.assertEqual(len(generators), 3)
        self.assertEqual(generators[0], "fixtureTestApp1.generator")

    def test_get_generators_all_apps_no_generators(self):
        for app in FIXTURE_TEST_APPS:
            self._remove_generator_from_app(app)
        generators = self.discoverer.get_generators(FIXTURE_TEST_APPS)
        self.assertEqual(len(generators), 0)
