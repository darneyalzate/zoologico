from src.services.entrada_service import EntradaService
from src.models.entrada_general  import EntradaGeneral
from src.models.entrada_infantil  import EntradaInfantil
from src.models.entrada_estudiante   import EntradaEstudiante
from src.models.pase_anual import PaseAnual

class Menu:
    def __init__(self):
        self.service = EntradaService()

    def registrar_entrada(self):
        print("\n📝 REGISTRO DE ENTRADA")

        print("""
Seleccione el tipo de entrada:
1. General
2. Infantil
3. Estudiante
4. Pase anual
""")

        opcion = input("Ingrese opción: ")

        tipos = {
            "1": EntradaGeneral,
            "2": EntradaInfantil,
            "3": EntradaEstudiante,
            "4": PaseAnual
        }

        if opcion not in tipos:
            print("❌ Opción inválida.")
            return

        clase = tipos[opcion]

        numero_documento = input("Número de documento: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        hora = input("Hora: ")
        dia = input("Día: ")
        guia = input("¿Requiere guía? (s/n): ").lower() == "s"

        entrada = clase(numero_documento, nombre, edad, hora, dia, guia)
        total = entrada.calcular_precio()
        data = entrada.to_dict(total)

        self.service.agregar(data)
        print(f"\n✅ Entrada registrada. Total pagado: ${total:,}\n")

    def listar_entradas(self):
        print("\n📄 ENTRADAS REGISTRADAS:\n")
        entradas = self.service.listar()

        if not entradas:
            print("⚠ No hay registros.")
            return

        for e in entradas:
            print("─" * 48)
            print(f"📌 TIPO: {e['tipo'].upper()}")
            print(f"📄 DOCUMENTO: {e['numero_documento']}")
            print(f"👤 NOMBRE: {e['nombre'].title()}")
            print(f"🎂 EDAD: {e['edad']} años")
            print(f"📅 DÍA: {e['dia']}")
            print(f"⏰ HORA: {e['hora']}")
            print(f"🧭 GUÍA: {'Sí' if e['guia'] else 'No'}")
            print(f"💲 TOTAL PAGADO: ${e['total_pagado']:,}".replace(",", "."))
            print("─" * 48)

    def iniciar(self):
        while True:
            print("""
📌 MENÚ PRINCIPAL
1. Registrar Entrada
2. Listar Entradas
3. Salir
""")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_entrada()
            elif opcion == "2":
                self.listar_entradas()
            elif opcion == "3":
                print("👋 Saliendo...")
                break
            else:
                print("❌ Opción inválida.")
