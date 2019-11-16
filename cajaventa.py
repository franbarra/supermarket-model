from producto import Producto

class CajaVenta():

    montoDebido = float()
    coste_total = float()
    dinero_recibido = float()
    bolsa_compras = []
    inventario = {}

    def __init__(self, checkout_items, inventario):
        self.bolsa_compras = checkout_items
        self.inventario = inventario

    def recibirDinero(self, monto):
        self.dinero_recibido += monto

    def agregarItemCarrito(self, item, lista):
        self.bolsa_compras = lista
        self.bolsa_compras.append(item)

    def displayItemsCarrito(self):
        print("\n####### Su Carrito #######\n")
        for index, codigo in enumerate(self.bolsa_compras):
            print(str(index+1) + ".", self.inventario[codigo]['Nombre'], "\t", self.inventario[codigo]['Precio'])
        print("\n")

    def escanearProducto(self):
        codigo_producto = int(input("\nPor favor ingrese el codigo de su producto: "))
        if codigo_producto not in [*self.inventario]:
            print("Este producto no se encuentra en nuestro inventario.")
        else:
            cantidad_a_vender = int(input("Cantidad del producto a vender? "))
            while cantidad_a_vender > self.inventario[codigo_producto]['Stock']:
                print("Esta cantidad no esta disponible.")
                print("La cantidad de producto disponible es: ", self.inventario[codigo_producto]['Stock'])
                cantidad_a_vender = int(input("Cantidad del producto a vender? "))
            else:
                for i in range(cantidad_a_vender):
                    self.bolsa_compras.append(codigo_producto)
        self.displayItemsCarrito()
        self.escanearOtro()
        return codigo_producto

    def escanearOtro(self):
        escanear = input("Escanear otro producto? (Y/N)")
        if(escanear == 'y' or escanear == 'Y'):
            self.escanearProducto()

    def calcularPago(self):
        carrito_items = self.bolsa_compras
        carrito_total = float(0)

        for codigo_de_producto in carrito_items:
            precio_del_producto = self.inventario[codigo_de_producto]['Precio']
            carrito_total += float(precio_del_producto)
            carrito_total = round(float(carrito_total), 2)
            self.inventario[codigo_de_producto]['Stock'] -= 1
        self.montoDebido = carrito_total
        return self.montoDebido

    def calcularVuelto(self, total):
        print("\nMonto debido: $", self.montoDebido)
        while self.montoDebido > self.dinero_recibido:
            vueltoCliente = round((self.montoDebido - self.dinero_recibido), 2)
            print("Paga restante: $" + str(vueltoCliente) + ", por favor ingrese un monto a pagar: ")
            prompt = round(float(input()), 2)
            if prompt < 0:
                print("Monto invalido.")
            else:
                self.recibirDinero(prompt)
        vueltoCliente = float(total) - self.dinero_recibido
        return vueltoCliente*-1

    def imprimirRecibo(self, vuelto):
        print("\n----- Recibo Fiscal -----\n")
        vuelto = round((float(vuelto)), 2)


        for codigo in self.bolsa_compras:
            print(self.inventario[codigo]['Nombre'], '     $' + str(self.inventario[codigo]['Precio']))

        print("\n")
        print("Total monto debido:\t", '$' + str(self.montoDebido))
        print("Monto recibido:\t", '$' + str(self.dinero_recibido))
        print("Vuelto entregado:\t", '$' + str(vuelto), '\n')
