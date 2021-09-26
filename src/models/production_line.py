from src.list.generic.g_list import *

class ProductionLine:

    def __init__(self, number = None, qt_components = None, assembly_time = None):
        self.number = number
        self.qt_components = qt_components
        self.assembly_time = assembly_time
        self.missing_assembly_time = assembly_time
        self.position = 0
        self.pending = GList()
        self.assemble = False