import xml.etree.ElementTree as ET
from src.models.project_singleton import *
from src.models.simulation import *
from src.models.product import *
from src.list.products.products_list import *

class SimulationController:

    def __init__(self):
        self.file_path = ProjectSingleton().file_simulation
        ProjectSingleton().simulation = Simulation(
            name = self.get_name(),
            products_list = self.get_products()
        )

    def get_name(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        for element in root:
            if element.tag == "Nombre":
                return str(element.text)

    def get_products(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        products_list = ProductsList()
        for element in root:

            if element.tag == "ListadoProductos":
                
                for product in element:
                    
                    product_found = ProjectSingleton().machine.products_list.search(name = product.text)
                    if product_found != None:
                        products_list.insert(product = product_found)

        return products_list