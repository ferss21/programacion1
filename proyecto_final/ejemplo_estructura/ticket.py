"""Modelo inicial de un ticket del proyecto final."""

class Ticket:
    def __init__(self, titulo, descripcion, categoria, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.prioridad = prioridad
        self.estado = "Abierto"

    def mostrar_resumen(self):
        return f"{self.titulo} - {self.prioridad} - {self.estado}"
