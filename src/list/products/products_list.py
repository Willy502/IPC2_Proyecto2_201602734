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

    def search(self, name):
        current = self.first
        while current != None:
            if current.product.name == name:
                return current.product
            current = current.next
        return None

    def size(self):
        length = 0
        current = self.first
        while current != None:
            length += 1
            current = current.next
        return length

    def get(self, position):
        length = 0
        current = self.first
        while current != None:
            length += 1
            if position == length - 1:
                return current.product
            current = current.next
        raise Exception('Products list out of range exception')
