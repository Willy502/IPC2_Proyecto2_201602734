import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from src.models.project_singleton import *
from src.controllers.machine_controller import *
from src.controllers.simulation_controller import *

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

        #TAB 1

        entry_machine = ttk.Entry(tab1, state = tk.DISABLED)
        entry_machine.grid(column = 0, row = 0)
        button_machine = ttk.Button(tab1, text = "Cargar máquina", command = lambda:self.on_click(option_clicked=1, entry=entry_machine)).grid(column = 1, row = 0)
        entry_simulation = ttk.Entry(tab1, state = tk.DISABLED)
        entry_simulation.grid(column = 0, row = 1)
        button_simulation = ttk.Button(tab1, text = "Cargar simulación", command = lambda:self.on_click(option_clicked=2, entry=entry_simulation)).grid(column = 1, row = 1)

        #TAB 2

        ttk.Label(tab2, text ="Product Name").grid(column = 0, row = 0)
        ttk.Label(tab2, text ="Componentes necesarios").grid(column = 0, row = 1)

        tv = ttk.Treeview(tab2)
        tv.grid(column = 1, row = 0)
        tv['columns'] = ('line1', 'linen')
        tv.heading("#0", text='Tiempo', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('line1', text='Linea 1')
        tv.column('line1', anchor='center', width=100)
        tv.heading('linen', text='Linea N')
        tv.column('linen', anchor='center', width=100)

        #TAB 3

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

        if option_clicked == 2 and ProjectSingleton().file_machine == None:
            messagebox.showinfo("Error", "Primero debes cargar una máquina")
            return

        file = fd.askopenfilename(title='Open file', filetypes=[('text files', '*.xml')])

        if file != "":

            entry.configure(state=tk.NORMAL)
            entry.delete(0, tk.END)
            entry.insert(0, file)
            entry.configure(state=tk.DISABLED)

            if option_clicked == 1:
                ProjectSingleton().file_machine = file
                MachineController()
            elif option_clicked == 2:
                ProjectSingleton().file_simulation = file
                SimulationController()

        else:
            messagebox.showinfo("Error", "No se ha cargado ningún archivo")

    def on_change_tab(self, event):
        name = self.tabControl.select()
        index = self.tabControl.index(name)
        if index == 1 and (ProjectSingleton().file_machine is None or ProjectSingleton().file_simulation is None):
            self.tabControl.select(0)
            messagebox.showinfo("Error", "No has cargado la máquina o el archivo de simulación")