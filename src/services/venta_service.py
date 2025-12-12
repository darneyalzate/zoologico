import datetime

class VentaService:
    def generar_ticket(self, entrada, total):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ticket = f"""
================= 🎟 TICKET DE ENTRADA 🎟 =================
Fecha: {fecha}
------------------------------------------------------------
Documento: {entrada.numero_documento}
Nombre: {entrada.nombre}
Edad: {entrada.edad}
Día de ingreso: {entrada.dia}
Hora: {entrada.hora}
¿Guía turística?: {"Sí" if entrada.guia else "No"}
Tipo de entrada: {entrada.__class__.__name__.upper()}
------------------------------------------------------------
TOTAL PAGADO: ${total:,}
============================================================
"""
        return ticket
