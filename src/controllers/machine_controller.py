import xml.etree.ElementTree as ET
from src.models.project_singleton import *
from src.models.production_line import *
from src.models.machine import *
from src.list.production_line.production_line_list import *
from src.models.product import *
from src.list.products.products_list import *

class MachineController:

    def __init__(self):
        self.file_path = ProjectSingleton().file_machine
        ProjectSingleton().machine = Machine(
            qt_production_lines = self.production_lines_qt(),
            production_lines_list = self.build_production_line_list(),
            products_list = self.build_products_list()
        )

    def production_lines_qt(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        for element in root:
            if element.tag == "CantidadLineasProduccion":
                return int(element.text)

    def build_production_line_list(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        production_line_list = ProductionLineList()
        for element in root:
            
            if element.tag == "ListadoLineasProduccion":

                for production_line in element:

                    pr_l = ProductionLine()
                    for production_element in production_line:

                        if production_element.tag == "Numero":
                            pr_l.number = int(production_element.text)
                        elif production_element.tag == "CantidadComponentes":
                            pr_l.qt_components = int(production_element.text)
                        elif production_element.tag == "TiempoEnsamblaje":
                            pr_l.assembly_time = int(production_element.text)
                    
                    production_line_list.insert(production_line = pr_l)

        return production_line_list

    def build_products_list(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        products_list = ProductsList()
        for element in root:

            if element.tag == "ListadoProductos":
                
                for product in element:
                    
                    prod = Product()
                    for product_element in product:
                        
                        if product_element.tag == "nombre":
                            prod.name = str(product_element.text)
                        elif product_element.tag == "elaboracion":
                            prod.build_instructions = str(product_element.text)

                    products_list.insert(product = prod)

        return products_list