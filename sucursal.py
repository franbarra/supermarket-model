'''
|HECHO| Agregar un nuevo producto.
|HECHO| Eliminar un producto dado su código.
|HECHO| Listar todos los productos de una forma prolija.
|HECHO| Actualizar el stock cuando se vende un producto.
|HECHO| Actualizar el precio unitario de un producto determinado en un cierto procentaje.
|HECHO| Determinar la existencia de un producto para poder vender la cantidad solicitada.
|HECHO| Reponer un producto cuando el stock está por debajo de un mínimo requerido.
2 Pedir los datos de un cliente para hacer envío a domicilio.
4 Determinar cuál es el artículo más vendido.
|HECHO| Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén
vencidos.
|HECHO| Simular la venta a un cliente y emitir el ticket de venta.
2 Agregar información adicional al producto para saber si un determinado producto tiene o no
descuento.
1 Si el producto vence en una semana hacer un 10% de descuento.
4 Determinar el producto más vendido dependiendo del tipo de producto.
'''

from supermercado import Supermercado
from producto import Producto
from cajaventa import CajaVenta
from pprint import pprint

miSupermercado = Supermercado()
checkout_items = []
inventario = {100: {'Precio': 40.31, 'Stock': 3, 'Nombre': 'Leche, 1L', 'Vto': '10-11-19'},
              101: {'Precio': 230.15, 'Stock': 8, 'Nombre': 'Queso, 500g', 'Vto': '09-12-19'},
              102: {'Precio': 96.10, 'Stock': 6, 'Nombre': 'Banana, 1kg', 'Vto': '18-04-19'},
              103: {'Precio': 34.99, 'Stock': 6, 'Nombre': 'Cuchara', 'Vto': '30-03-46'},
              104: {'Precio': 552, 'Stock': 23, 'Nombre': 'Juego Cuchillos', 'Vto': '30-04-50'},
              105: {'Precio': 20.13, 'Stock': 12, 'Nombre': 'Chicles', 'Vto': '30-10-30'},
              106: {'Precio': 8.99, 'Stock': 1, 'Nombre': 'Lapicera', 'Vto': '30-01-50'},
              107: {'Precio': 136.44, 'Stock': 43, 'Nombre': 'Naranja, 1kg', 'Vto': '12-12-19'},
              108: {'Precio': 80.88, 'Stock': 72, 'Nombre': 'Pimienta, 100gr', 'Vto': '13-04-20'}}

miSupermercado.setInventario(inventario)

def cobrarCliente():
    caja1 = CajaVenta(checkout_items, inventario)
    caja1.escanearProducto()
    total_pagado = caja1.calcularPago()
    vuelto = caja1.calcularVuelto(total_pagado)
    caja1.imprimirRecibo(vuelto)
    print("\nGracias por comprar en nuestra sucursal")

    next = input("(P)roximo cliente o (S)alir? ")
    if(next == "p" or next == "P"):
        procesoPrincipal()
    else:
        exit()


print("\nPor favor elija una de las siguientes opciones: \n")
print("1. Cobrar a cliente en caja")
print("2. Administrar supermercado")
print("3. Informacion Extra/Clientes")
eleccion_usuario = int(input())

if eleccion_usuario == 1:
    print("\n--------Bienvenido/a a Sucursal Dia!--------\n")
    cobrarCliente()
if eleccion_usuario == 2:
    miSupermercado.administrarSupermercado()
else:
    exit()
