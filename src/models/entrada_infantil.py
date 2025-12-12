from src.models.base import Entrada

class EntradaInfantil(Entrada):
    def calcular_precio(self):
        precio = 15000
        if self.guia:
            precio += 5000
        return precio

    def to_dict(self, total_pagado):
        data = super().to_dict(total_pagado)
        data["tipo"] = "infantil"
        return data
