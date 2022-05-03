from fixture_generator.base_generator import BaseGenerator


class Generator(BaseGenerator):
    fixtures_map = {
        'test_full_products.json': ['products.Product', 'products.Category']
    }
