from inventario import Inventario
from producto import Producto

def cargar_inventario_inicial(inventario):
    if not inventario.lista_productos:
        inventario: (Producto("101", "Blusa roja", "ropa", 15, 29))
        inventario: (Producto("102", "Pantalón jeans", "ropa", 20, 39))
        inventario: (Producto("201", "Labial mate rosa", "maquillaje", 30, 12))
        inventario: (Producto("202", "Sombra de ojos nude", "maquillaje", 25, 18))

def ejecutar_menu():
    inventario = Inventario()
    cargar_inventario_inicial(inventario)

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_prod = input("ID del producto: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría (ropa/maquillaje): ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar(Producto(id_prod, nombre, categoria, cantidad, precio))
            except ValueError:
                print("Cantidad o precio inválidos.")

        elif opcion == "2":
            id_prod = input("ID a eliminar: ")
            inventario.eliminar(id_prod)

        elif opcion == "3":
            id_prod = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para no cambiar): ")
            precio = input("Nuevo precio (Enter para no cambiar): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar(id_prod, cantidad, precio)
            except ValueError:
                print("Cantidad o precio inválidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar(nombre)

        elif opcion == "5":
            inventario.mostrar()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_menu()