from src.models.base import Entrada

class EntradaGeneral(Entrada):
    def calcular_precio(self):
        precio = 25000
        if self.guia:
            precio += 10000
        return precio

    def to_dict(self, total_pagado):
        data = super().to_dict(total_pagado)
        data["tipo"] = "general"
        return data
