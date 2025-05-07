class Producto:
    def __init__(self, nombre=None, cantidad=None, precio=None, categoria=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return(f'Nombre: {self.nombre} - Cantidad: {self.cantidad} - Precio: {self.precio} - Categoria: {self.categoria}')
