# Menú interactivo para la gestión de inventario en una tienda de ropa y maquillaje
from inventario import Inventario
from producto import Producto

def cargar_inventario_inicial(inventario):
    """Función para precargar algunos productos de ropa y maquillaje"""
    inventario:(Producto("101", "Blusa roja", "ropa", 15, 29))
    inventario:(Producto("102", "Pantalón jeans", "ropa", 20, 39))
    inventario:(Producto("201", "Labial mate rosa", "maquillaje", 30, 12))
    inventario:(Producto("202", "Sombra de ojos nude", "maquillaje", 25, 18))


def ejecutar_menu():
    inventario = Inventario()
    cargar_inventario_inicial(inventario)  # <<< Precarga los productos

    while True:
        print("\n===== SISTEMA DE INVENTARIO - TIENDA DE ROPA Y MAQUILLAJE =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario completo")
        print("6. Salir")
        print("===============================================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_prod = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría (ropa/maquillaje): ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio: "))
            nuevo = Producto(id_prod, nombre, categoria, cantidad, precio)
            inventario.agregar(nuevo)

        elif opcion == "2":
            id_prod = input("ID del producto a eliminar: ")
            inventario.eliminar(id_prod)

        elif opcion == "3":
            id_prod = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para no cambiar): ")
            precio = input("Nuevo precio (Enter para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar(id_prod, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar(nombre)

        elif opcion == "5":
            inventario.mostrar()

        elif opcion == "6":
            print("Saliendo del sistema. Hasta luego.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar_menu()