
class Producto:
    '''Modelo de un producto en un supermercado'''

    codigo = int()
    descripcion = ''
    stock = int()
    precio_unitario = float()
    fecha_vencimiento = ''
    tipo_de_producto = ''

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.descripcion = nombre

    def getCodigo(self):
        return self.codigo

    def getDescripcion(self):
        return self.descripcion

    def getStock(self):
        return self.stock

    def getPrecioUnitario(self):
        return self.precio_unitario

    def getFechaVencimiento(self):
        return self.fecha_vencimiento

    def getTipoProducto(self):
        return self.tipo_de_producto

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setStock(self, stock):
        self.stock = stock

    def setPrecioUnitario(self, precio):
        self.precio_unitario = precio

    def setFechaVencimiento(self, fecha):
        self.fecha_vencimiento = fecha

    def setTipoProducto(self, tipo):
        self.tipo_de_producto = tipo
