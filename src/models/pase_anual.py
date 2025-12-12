from src.models.base import Entrada

class PaseAnual(Entrada):
    def calcular_precio(self):
        precio = 140000
        if self.guia:
            precio += 10000
        return precio

    def to_dict(self, total_pagado):
        data = super().to_dict(total_pagado)
        data["tipo"] = "pase_anual"
        return data
