import tkinter as tk
from tkinter import ttk
import pickle
import os.path 

#Programador: Barajas Zavala Ulises
#02/02/2024

class Directorio:
    
    def __init__(self):
        self.contactos = []

    def agregar(self, nombre: str, numero: str):
        lista = [nombre, numero]
        self.contactos.append(lista)
    def getLen(self):
        return len(self.contactos)
    
    def getContacto(self, index: int):
        return self.contactos[index]


class CheckPointingGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Checkpointing con pickle")
        self.data = Directorio()

        self.lotesP = tk.StringVar()
        self.lotesP.set('0')

        if 1==1:
            frameC = tk.Frame(root)
            frameC.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

            tk.Label(frameC, text="Captura", font=('Roboto', 14), justify='center').grid(row=0, column=0, pady=5, padx=5, sticky="w")

            tk.Label(frameC, text="Nombre(Completo):").grid(row=1, column=0, pady=5, padx=5, sticky="w")
            self.entryNombre = ttk.Entry(frameC, width=20)
            self.entryNombre.grid(row=1, column=1, pady=5, padx=5, sticky="w")

            tk.Label(frameC, text="Numero(Tel):").grid(row=2, column=0, pady=5, padx=5, sticky="w")
            self.entryNumero = ttk.Entry(frameC, width=20)
            self.entryNumero.grid(row=2, column=1, pady=5, padx=5, sticky="w")

            ttk.Button(frameC, text="Capturar", command=self.capturar).grid(row=3, column=1, pady=5, padx=5, sticky="w")

            ttk.Separator(frameC, orient='horizontal', style='TSeparator').grid(row=4, column=0,columnspan=2, sticky='ew', pady=5)      
            tk.Label(frameC, text="Contactos:").grid(row=5, column=0, pady=5, padx=5, sticky="w")
            tk.Label(frameC, textvariable=self.lotesP).grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
        if 3==3:
            frameLT = tk.Frame(root)
            frameLT.grid(row=0, column=1, rowspan=5, padx=5, pady=5, sticky="nsew")
            tk.Label(frameLT, text="Directorio", font=('Roboto',12), justify='center').grid(row=0, column=0, pady=5, padx=5, sticky="w")
            self.treeLT = ttk.Treeview(frameLT, columns=('C1', 'C2'), show='headings')
            self.treeLT.heading('C1', text='Nombre')
            self.treeLT.heading('C2', text='Telefono')
            for col in ('C1', 'C2'):
                self.treeLT.column(col, width=140, anchor='center')

            scrollbar_y = ttk.Scrollbar(frameLT, orient='vertical', command=self.treeLT.yview)
            self.treeLT.configure(yscrollcommand=scrollbar_y.set)

            self.treeLT.grid(row=1, column=0, sticky='nsew')
            scrollbar_y.grid(row=1, column=1, sticky='ns')

            frameLT.rowconfigure(0, weight=1)
            frameLT.columnconfigure(0, weight=1)
            
        if os.path.isfile("directorio.pickle"):
            self.restablecerData()

    def capturar(self):
        self.data.agregar( self.entryNombre.get(), self.entryNumero.get())

        self.lotesP.set(str(self.data.getLen()))

        self.treeLT.insert("", "end", values=self.data.getContacto(self.data.getLen()-1))

        self.entryNombre.delete(0, tk.END)
        self.entryNumero.delete(0, tk.END)

        with open('directorio.pickle', 'wb') as file:
            pickle.dump(self.data, file) 
        
    def restablecerData(self):
        with open('directorio.pickle', 'rb') as file:
            self.data: Directorio = pickle.load(file)
        for contacto in self.data.contactos:
            self.treeLT.insert("", "end", values=contacto)
        self.lotesP.set(str(self.data.getLen()))
    

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckPointingGUI(root)
    root.mainloop()
            
        