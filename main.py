class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def agregar_descuento (self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento