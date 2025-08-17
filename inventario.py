# Clase que gestiona los productos de la tienda
from producto import Producto

class Inventario:
    def _init_(self):
        self.lista_productos = []

    def agregar(self, producto):
        # Verificar que el ID sea único
        if any(p.obtener_id() == producto.obtener_id() for p in self.lista_productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.lista_productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar(self, id_producto):
        for p in self.lista_productos:
            if p.obtener_id() == id_producto:
                self.lista_productos.remove(p)
                print("Producto eliminado.")
                return
        print("No se encontró ningún producto con ese ID.")

    def actualizar(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.lista_productos:
            if p.obtener_id() == id_producto:
                if nueva_cantidad is not None:
                    p.cambiar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.cambiar_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("No se encontró ningún producto con ese ID.")

    def buscar(self, texto):
        resultados = [p for p in self.lista_productos if texto.lower() in p.obtener_nombre().lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for p in resultados:
                print(" ", p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual de la tienda de ropa y maquillaje:")
            for p in self.lista_productos:
                print(" ", p)