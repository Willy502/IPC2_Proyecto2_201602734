import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from src.models.project_singleton import *

class Gui:

    def __init__(self):
        self.build_gui()

    def build_gui(self):
        self.root = tk.Tk()
        self.root.title("Línea de ensamblaje")
        self.tabControl = ttk.Notebook(self.root, width = 500, height = 500)
  
        tab1 = ttk.Frame(self.tabControl)
        tab2 = ttk.Frame(self.tabControl)
        tab3 = ttk.Frame(self.tabControl)
        
        self.tabControl.add(tab1, text ='Cargar Archivos')
        self.tabControl.add(tab2, text ='Ejecutar ensamblaje')
        self.tabControl.add(tab3, text ='Ayuda')
        self.tabControl.pack(expand = True, fill = tk.BOTH)

        entry_machine = ttk.Entry(tab1, state = tk.DISABLED)
        entry_machine.grid(column = 0, row = 0)
        button_machine = ttk.Button(tab1, text = "Cargar máquina", command = lambda:self.on_click(option_clicked=1, entry=entry_machine)).grid(column = 1, row = 0)
        entry_simulation = ttk.Entry(tab1, state = tk.DISABLED)
        entry_simulation.grid(column = 0, row = 1)
        button_simulation = ttk.Button(tab1, text = "Cargar simulación", command = lambda:self.on_click(option_clicked=2, entry=entry_simulation)).grid(column = 1, row = 1)

        ttk.Label(tab2,
                text ="Lets dive into the\
                world of computers").grid(column = 0,
                                            row = 0, 
                                            padx = 30,
                                            pady = 30)

        ttk.Label(tab3, text =  self.information()).grid(column = 0, row = 0)

        self.root.bind("<Button>", self.on_change_tab)
        self.root.mainloop()

    def information(self):
        info = "Wilfred Alejandro Barrios Ola \n"
        info += "201602734 \n"
        info += "Introducción a la programación y computación 2 \n"
        info += "Sección  \n"
        return info

    def on_click(self, option_clicked, entry):

        file = fd.askopenfilename(title='Open file', filetypes=[('text files', '*.xml')])

        if file != "":

            entry.configure(state=tk.NORMAL)
            entry.delete(0, tk.END)
            entry.insert(0, file)
            entry.configure(state=tk.DISABLED)

            if option_clicked == 1:
                ProjectSingleton().file_machine = file
            elif option_clicked == 2:
                ProjectSingleton().file_simulation = file

        else:
            messagebox.showinfo("Error", "No se ha cargado ningún archivo")

    def on_change_tab(self, event):
        name = self.tabControl.select()
        index = self.tabControl.index(name)
        if index == 1 and (ProjectSingleton().file_machine is None or ProjectSingleton().file_simulation is None):
            self.tabControl.select(0)
            messagebox.showinfo("Error", "No has cargado la máquina o el archivo de simulación")