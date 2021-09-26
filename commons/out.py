import xml.etree.cElementTree as ET
from xml.dom import minidom

class Out:

    def build_output_xml(self, products_list, instructions_list, nombre_simulacion = "Producto Individual"):
        root = ET.Element("SalidaSimulacion")
        name_sim = ET.SubElement(root, "Nombre").text = nombre_simulacion

        listado_productos = ET.SubElement(root, "ListadoProductos")
        for i in range(0, products_list.size()):
            prod = ET.SubElement(listado_productos, "producto")
            name = ET.SubElement(prod, "nombre").text = products_list.get(i).name
            inside_instructions_list = instructions_list.get(i)
            total_time = ET.SubElement(prod, "TiempoTotal").text = str(instructions_list.get(i).get(inside_instructions_list.size() - 1).get(0))
            optimo = ET.SubElement(prod, "ElaboracionOptima")
            for index in range(0, inside_instructions_list.size()):
                line_instruction = inside_instructions_list.get(index)
                time = ET.SubElement(optimo, "Tiempo", NoSegundo=str(line_instruction.get(0)))
                for inside_index in range(1, line_instruction.size()):
                    lineaEnsamble = ET.SubElement(time, "LineaEnsamblaje", NoLinea=str(inside_index)).text = line_instruction.get(inside_index)

        data = minidom.parseString(ET.tostring(root))
        file = open("output/output.xml", "w")
        new_data = data.toprettyxml()
        file.write(new_data)
