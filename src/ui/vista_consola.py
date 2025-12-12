def mostrar_entradas(entradas):
    print("\n=== REGISTRO DE VENTAS ===")
    for e in entradas:
        e.registrar_ingreso()
        print(f"- Tipo: {e.__class__.__name__} | Precio: ${e.calcular_precio()} | Válida: {e.validar_entrada()}")

def mostrar_estadisticas(ingresos, total):
    print("\n=== ESTADÍSTICAS ===")
    print(f"Total de entradas vendidas: {total}")
    print(f"Ingresos generados: ${ingresos}")
