import json
import os

class ReporteService:
    def __init__(self):
        self.ruta = "data/entradas.json"

    def cargar(self):
        if not os.path.exists(self.ruta):
            return []
        with open(self.ruta, "r") as f:
            return json.load(f)

    def generar_reportes(self):
        entradas = self.cargar()
        if not entradas:
            return None

        total_vendidas = len(entradas)
        total_recaudado = sum(e["total_pagado"] for e in entradas)

        por_tipo = {}
        for e in entradas:
            t = e["tipo"]
            por_tipo[t] = por_tipo.get(t, 0) + 1

        con_guia = sum(1 for e in entradas if e["guia"])

        edades = [int(e["edad"]) for e in entradas]
        promedio_edad = sum(edades) / len(edades)

        dias = {}
        for e in entradas:
            dia = e["dia"].lower()
            dias[dia] = dias.get(dia, 0) + 1

        dia_mas_visitado = max(dias, key=dias.get)

        return {
            "total_vendidas": total_vendidas,
            "total_recaudado": total_recaudado,
            "por_tipo": por_tipo,
            "con_guia": con_guia,
            "promedio_edad": round(promedio_edad, 2),
            "dia_mas_visitado": dia_mas_visitado.title()
        }
