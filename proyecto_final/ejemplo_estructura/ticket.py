"""Modelo inicial de solicitudes y variantes para el proyecto final."""


class Solicitud:
    """Datos y comportamiento compartidos por las solicitudes de soporte."""

    ESTADOS = ("Abierta", "En proceso", "Cerrada")

    def __init__(self, titulo, descripcion, categoria, prioridad, reportado_por):
        self.titulo = titulo.strip()
        self.descripcion = descripcion.strip()
        self.categoria = categoria.strip()
        self.prioridad = prioridad
        self.reportado_por = reportado_por.strip()
        self.estado = "Abierta"

    def mostrar_resumen(self):
        """Devuelve una descripción breve; las subclases pueden especializarla."""
        return f"{self.titulo} - {self.prioridad} - {self.estado}"


class SolicitudUrgente(Solicitud):
    """Solicitud que registra una razón de urgencia."""

    def __init__(self, titulo, descripcion, categoria, prioridad, reportado_por, motivo):
        super().__init__(titulo, descripcion, categoria, prioridad, reportado_por)
        self.motivo = motivo

    def mostrar_resumen(self):
        return f"URGENTE: {super().mostrar_resumen()} - {self.motivo}"


class SolicitudConsulta(Solicitud):
    """Solicitud destinada a una consulta o petición de información."""

    def mostrar_resumen(self):
        return f"CONSULTA: {super().mostrar_resumen()}"
