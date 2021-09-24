from .production_line_node import *

class ProductionLineList:

    def __init__(self):
        self.first = None

    def insert(self, production_line):
        if self.first is None:
            self.first = ProductionLineNode(production_line = production_line)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = ProductionLineNode(production_line = production_line)
