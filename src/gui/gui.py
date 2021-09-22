import tkinter as tk
from tkinter import ttk


class Gui:

    def __init__(self):
        self.build_gui()

    def build_gui(self):
        self.root = tk.Tk()
        self.root.title("Línea de ensamblaje")
        tabControl = ttk.Notebook(self.root, width = 500, height = 500)
  
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        
        tabControl.add(tab1, text ='Cargar Archivos')
        tabControl.add(tab2, text ='Ejecutar ensamblaje')
        tabControl.add(tab3, text ='Ayuda')
        tabControl.pack(expand = True, fill = tk.BOTH)
        
        ttk.Label(tab1, 
                text ="Welcome to \
                GeeksForGeeks").grid(column = 0, 
                                    row = 0,
                                    padx = 30,
                                    pady = 30)  
        ttk.Label(tab2,
                text ="Lets dive into the\
                world of computers").grid(column = 0,
                                            row = 0, 
                                            padx = 30,
                                            pady = 30)

        ttk.Label(tab3, text =  self.information()).grid(column = 0,
                                            row = 0)
        self.root.mainloop()

    def information(self):
        info = "Wilfred Alejandro Barrios Ola \n"
        info += "201602734 \n"
        info += "Introducción a la programación y computación 2 \n"
        info += "Sección  \n"
        return info