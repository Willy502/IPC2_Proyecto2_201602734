from .products_node import *

class ProductsList:

    def __init__(self):
        self.first = None

    def insert(self, product):
        if self.first is None:
            self.first = ProductsNode(product = product)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = ProductsNode(product = product)
