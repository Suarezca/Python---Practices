class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f'{self.codigo}: {self.nombre} - Precio: ${self.precio:.2f} - Cantidad: {self.cantidad}'
        
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad


class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
        
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
            
    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto is not None:
            if producto.cantidad >= cantidad:
                producto.actualizar_cantidad(producto.cantidad - cantidad)
                print(f'Se vendieron {cantidad} unidades de {producto.nombre}.')
            else:
                print('No hay suficientes unidades en el inventario.')
        else:
            print('El producto no está en el inventario.')


inventario = Inventario()

producto1 = Producto('P01', 'Camisa', 29.99, 100)
producto2 = Producto('P02', 'Pantalón', 49.99, 50)
producto3 = Producto('P03', 'Zapatos', 99.99, 25)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

inventario.mostrar_productos()

producto2.actualizar
