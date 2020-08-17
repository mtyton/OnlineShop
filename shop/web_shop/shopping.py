

class CartProduct(object):
    product = None
    quantity = 0

    def create_rpoduct(self, product):
        self.product = product
        self.quantity = 1

    def update_product_number(self):
        pass


class ShoppingCart(object):
    product_list = []

    def add_product_to_cart(self, product):
        if product.is_available():
            self.product_list.append(product)
            return True
        else:
            return False

    def remove_product_from_cart(self, product):
        if product in self.product_list:
            self.product_list.pop(product)
            return True
        else:
            return False