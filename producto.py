class Producto:
    def __init__(self, id_producto, nombre, categoria, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre1

    def obtener_categoria(self):
        return self.categoria

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    def cambiar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def _str_(self):
        return f"[{self.id}] {self.nombre} ({self.categoria}) - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_linea(self):
        return f"{self.id},{self.nombre},{self.categoria},{self.cantidad},{self.precio}\n"

    @classmethod
    def from_linea(cls, linea):
        id_producto, nombre, categoria, cantidad, precio = linea.strip().split(',')
        return cls(id_producto, nombre, categoria, int(cantidad), float(precio))