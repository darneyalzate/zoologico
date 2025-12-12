from src.services.entrada_service import EntradaService
from src.services.reporte_service import ReporteService
from src.services.venta_service import VentaService

from src.models.entrada_general import EntradaGeneral
from src.models.entrada_infantil import EntradaInfantil
from src.models.entrada_estudiante import EntradaEstudiante
from src.models.pase_anual import PaseAnual


class Menu:
    def __init__(self):
        self.service = EntradaService()
        self.reportes = ReporteService()
        self.ventas = VentaService()

    def iniciar(self):
        while True:
            print("\n📌 MENÚ PRINCIPAL")
            print("1. Registrar Entrada")
            print("2. Listar Entradas")
            print("3. Reportes")
            print("4. Salir")

            op = input("Seleccione una opción: ")

            if op == "1":
                self.registrar_entrada()
            elif op == "2":
                self.listar_entradas()
            elif op == "3":
                self.mostrar_reportes()
            elif op == "4":
                break
            else:
                print("⚠ Opción inválida.")

    def registrar_entrada(self):
        print("\n📝 REGISTRO DE ENTRADA")
        print("1. General")
        print("2. Infantil")
        print("3. Estudiante")
        print("4. Pase Anual")

        tipo = input("Seleccione el tipo: ")

        numero = input("Número de documento: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        hora = input("Hora: ")
        dia = input("Día: ")
        guia = input("¿Guía? (s/n): ").lower() == "s"

        if tipo == "1":
            entrada = EntradaGeneral(numero, nombre, edad, hora, dia, guia)
        elif tipo == "2":
            entrada = EntradaInfantil(numero, nombre, edad, hora, dia, guia)
        elif tipo == "3":
            entrada = EntradaEstudiante(numero, nombre, edad, hora, dia, guia)
        elif tipo == "4":
            entrada = PaseAnual(numero, nombre, edad, hora, dia, guia)
        else:
            print("⚠ Tipo inválido.")
            return

        total = entrada.calcular_precio()
        data = entrada.to_dict(total)

        self.service.registrar(data)

        ticket = self.ventas.generar_ticket(entrada, total)
        print(ticket)

        print("✅ Entrada registrada correctamente.")

    def listar_entradas(self):
        print("\n📄 ENTRADAS REGISTRADAS:\n")
        entradas = self.service.listar()

        if not entradas:
            print("No hay entradas registradas.")
            return

        for e in entradas:
            print("─" * 48)
            print(f"Tipo: {e['tipo'].title()}")
            print(f"Documento: {e['numero_documento']}")
            print(f"Nombre: {e['nombre']}")
            print(f"Edad: {e['edad']}")
            print(f"Hora: {e['hora']}")
            print(f"Día: {e['dia']}")
            print(f"Guía: {'Sí' if e['guia'] else 'No'}")
            print(f"Total pagado: ${e['total_pagado']:,}")
            print("─" * 48)

    def mostrar_reportes(self):
        r = self.reportes.generar_reportes()

        if not r:
            print("⚠ No hay datos para reportar.")
            return

        print("\n📊 REPORTES DEL ZOOLÓGICO")
        print("Total entradas vendidas:", r["total_vendidas"])
        print("Total dinero recaudado: $", r["total_recaudado"])
        print("Entradas por tipo:", r["por_tipo"])
        print("Entradas con guía:", r["con_guia"])
        print("Promedio edad:", r["promedio_edad"])
        print("Día con más visitas:", r["dia_mas_visitado"])
