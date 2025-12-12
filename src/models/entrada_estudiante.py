from src.models.base import Entrada

class EntradaEstudiante(Entrada):
    def calcular_precio(self):
        precio = 20000
        if self.guia:
            precio += 6000
        return precio

    def to_dict(self, total_pagado):
        data = super().to_dict(total_pagado)
        data["tipo"] = "estudiante"
        return data
