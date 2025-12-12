from abc import ABC, abstractmethod

class Entrada(ABC):
    def __init__(self, numero_documento, nombre, edad, hora, dia, guia):
        self.numero_documento = numero_documento
        self.nombre = nombre
        self.edad = int(edad)
        self.hora = hora
        self.dia = dia
        self.guia = guia

    @abstractmethod
    def calcular_precio(self):
        pass

    def to_dict(self, total_pagado):
        return {
            "numero_documento": self.numero_documento,
            "nombre": self.nombre,
            "edad": self.edad,
            "hora": self.hora,
            "dia": self.dia,
            "guia": self.guia,
            "total_pagado": total_pagado
        }
