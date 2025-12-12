import json
import os

class EntradaService:
    def __init__(self):
        self.archivo = "entradas.json"
        self.entradas = []
        self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, "r") as f:
            self.entradas = json.load(f)

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self.entradas, f, indent=4)

    def agregar(self, entrada_dict):
        self.entradas.append(entrada_dict)
        self.guardar()

    def listar(self):
        return self.entradas
