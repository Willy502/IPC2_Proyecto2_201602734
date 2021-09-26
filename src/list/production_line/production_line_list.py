from .production_line_node import *

class ProductionLineList:

    def __init__(self):
        self.first = None

    def size(self):
        length = 0
        current = self.first
        while current != None:
            length += 1
            current = current.next
        return length

    def insert(self, production_line):
        if self.first is None:
            self.first = ProductionLineNode(production_line = production_line)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = ProductionLineNode(production_line = production_line)

    def search(self, number):
        current = self.first
        while current != None:
            if current.production_line.number == number:
                return current.production_line
            current = current.next
        return None

    def get(self, position):
        length = 0
        current = self.first
        while current != None:
            length += 1
            if position == length - 1:
                return current.production_line
            current = current.next
        raise Exception('Production line list out of range exception')
