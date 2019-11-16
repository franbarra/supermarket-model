from producto import Producto
from random import uniform
from pprint import pprint, pformat
from datetime import datetime, date

class Supermercado:

    lista_productos = []
    inventario = {}

    def __init__(self):
        pass

    def agregarUnoItem(self, codigo, lista):
        lista.append(codigo)

    def listarInventario(self, lista):
        self.inventario = lista
        print("#Producto#\t", "\t#Stock#", "\t#Precio#")
        print("{0:<}".format("-"*48))
        for key in [*self.inventario]:
            print("{0:<15}".format(self.inventario[key]['Nombre']),
                  "\t{0:^5}".format(self.inventario[key]['Stock']),
                  "\t{0:>15}".format(self.inventario[key]['Precio']))

    def setInventario(self, inventario_a_usar):
        self.inventario = inventario_a_usar

    def agregarProducto(self):
        print("Ingrese el nombre de un nuevo producto: ")
        nombre_nuevo_producto = str(input()).capitalize()
        codigo_nuevo_producto = max([*self.inventario]) + 1
        precio_nuevo_producto = float(input("Cuanto vale este nuevo producto? $"))
        stock_nuevo_producto = int(input("Cantidad de producto ingresando al stock? "))
        producto = {codigo_nuevo_producto: {'Precio': precio_nuevo_producto,
                                            'Stock': stock_nuevo_producto,
                                            'Nombre': nombre_nuevo_producto}}
        self.inventario.update(producto)
        self.listarInventario(self.inventario)
        return self.inventario

    def getProducto(self, codigo):
        self.descripcion = self.inventario[codigo]['Nombre']
        self.precio_unitario = self.inventario[codigo]['Precio']
        self.codigo = self.inventario[codigo]
        self.stock = self.inventario[codigo]['Stock']
        return {'Nombre': self.descripcion.capitalize(),
                'Precio': self.precio_unitario,
                'Stock': self.stock,
                'Codigo': self.codigo}

    def eliminarProductoVencido(self):
        '''Eliminar un producto que haya vencido, es decir, que su fecha
        de vencimiento sea menor a la del tiempo actual.'''
        hoy = datetime.now()
        productos_vencidos = {}
        print("")
        for key in [*self.inventario]:
            fecha_vencimiento = self.inventario[key]['Vto']
            fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%d-%m-%y')
            if fecha_vencimiento <= hoy:
                productos_vencidos[key] = self.inventario[key]
                print("Se ha removido el producto", self.inventario[key]['Nombre'], "de nuestro inventario por estar vencido.")
                del self.inventario[key]
            else:
                continue
        print("")
        print("Proceso terminado con exito")
        return productos_vencidos

    def eliminarProductoCodigo(self):
        codigo = int(input("Ingrese el codigo del producto que desea eliminar: "))
        if codigo in [*self.inventario]:
            print("El producto", self.inventario[codigo]['Nombre'], "ha sido eliminado.")
            self.inventario.pop(codigo, None)
        else:
            print("Codigo no encontrado")

    def reponerStock(self):
        for key in self.inventario:
            while self.inventario[key]['Stock'] < 5:
                print("Producto con stock insuficiente: ", self.inventario[key]['Nombre'])
                cantidad_a_reponer = int(input("Cuanto quiere reponer de stock? "))
                self.inventario[key]['Stock'] = cantidad_a_reponer

    def actualizarPrecioUnitario(self):
        codigo = int(input("Que producto desea modificar?(Ingresar codigo): "))
        porcentaje = float(input("En que porcentaje desea modificar el precio del producto? "))
        self.inventario[codigo]['Precio'] = round(float((self.inventario[codigo]['Precio']) * porcentaje), 2)
        print("El nuevo precio del producto es de: $" + str(self.inventario[codigo]['Precio']))
        return self.inventario[codigo]['Precio']

    def continuarAdministracion(self):
        continuar = input("Desea continuar con la administracion? (Y/N)")
        if continuar == 'y' or 'Y':
            self.administrarSupermercado()
        else:
            exit()

    def administrarSupermercado(self):
        '''Esta funcion tendria que ser llamada cuando el usuario eliga la opcion
        2, "administrar inventario"'''
        print("\nPor favor eliga una de las siguientes opciones: \n")
        print("1. Agregar Producto")
        print("2. Eliminar producto Vencido")
        print("3. Eliminar producto por Codigo")
        print("4. Listar Inventario")
        print("5. Actualizar precio")
        print("6. Reponer Stock")
        eleccion_usuario = int(input())
        if eleccion_usuario == 1:
            self.agregarProducto()
        if eleccion_usuario == 2:
            self.eliminarProductoVencido()
        if eleccion_usuario == 3:
            self.eliminarProductoCodigo()
        if eleccion_usuario == 4:
            self.listarInventario(self.inventario)
        if eleccion_usuario == 5:
            self.actualizarPrecioUnitario()
        if eleccion_usuario == 6:
            self.reponerStock()
