from graphviz import Digraph
from src.list.generic.g_list import *

class Graph:

    def build_graph(self, product):
        name_show = "IPC2_" + product.name
        dot = Digraph(comment=name_show, graph_attr={'rankdir':'LR', 'splines':'line'})

        instructions_list = GList()
        line_comp = ""

        # instructions list for a single product
        for letter in product.build_instructions:
            if ord(letter) == 32:
                instructions_list.add(line_comp)
                line_comp = ""
                continue
            line_comp += letter
        instructions_list.add(line_comp)

        counter_inst = 0
        for i in range(0, instructions_list.size()):
            dot.node(instructions_list.get(position = i) + str(counter_inst), instructions_list.get(position = i))
            counter_inst += 1

        counter_inst = 0
        for i in range(0, instructions_list.size()):
            if i != instructions_list.size() - 1:
                dot.edge(instructions_list.get(position = i) + str(counter_inst), instructions_list.get(position = i + 1) + str(counter_inst + 1))
                counter_inst += 1

        dot.render('output/IPC2_' + product.name + '.gv', view=True)
        file_name = dot.filepath + ".pdf"