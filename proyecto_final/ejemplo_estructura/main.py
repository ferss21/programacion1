"""Menú inicial para integrar las capas del sistema de solicitudes."""

from database import crear_tabla


def mostrar_menu():
    """Muestra las operaciones que deberá conectar el estudiante."""
    print("\n===== ATENCIÓN DE SOLICITUDES =====")
    print("1. Registrar solicitud")
    print("2. Mostrar solicitudes")
    print("3. Buscar solicitud")
    print("4. Actualizar solicitud")
    print("5. Cambiar estado")
    print("6. Exportar reporte")
    print("7. Eliminar solicitud")
    print("8. Salir")


crear_tabla()
mostrar_menu()
print("Conecte cada opción con las clases de solicitud y la base de datos.")
