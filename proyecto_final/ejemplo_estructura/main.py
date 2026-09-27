"""Menú inicial para integrar las capas del sistema de tickets."""

from database import crear_tabla


def mostrar_menu():
    """Muestra las operaciones que deberá conectar el estudiante."""
    print("\n===== SISTEMA DE TICKETS =====")
    print("1. Crear ticket")
    print("2. Mostrar tickets")
    print("3. Buscar ticket")
    print("4. Actualizar ticket")
    print("5. Cambiar estado")
    print("6. Eliminar ticket")
    print("7. Salir")


crear_tabla()
mostrar_menu()
print("Conecte cada opción con la clase Ticket y la base de datos.")
