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
        
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad,
        }
        
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
            
    def to_dict(self):
        return [producto.to_dict() for producto in self.productos]
        
class Tienda:
    def __init__(self, nombre, inventario):
        self.nombre = nombre
        self.inventario = inventario
        
    def __str__(self):
        return f'Tienda {self.nombre} - Inventario: {len(self.inventario.productos)} productos'
        
    def agregar_producto(self, codigo, nombre, precio, cantidad):
        producto = Producto(codigo, nombre, precio, cantidad)
        self.inventario.agregar_producto(producto)
        
    def mostrar_productos(self):
        self.inventario.mostrar_productos()
        
    def vender_producto(self, codigo, cantidad):
        self.inventario.vender_producto(codigo, cantidad)
        
    def generar_reporte(self):
        inventario_dict = self.inventario.to_dict()
        total_productos = len(inventario_dict)
        total_cantidad = sum([producto['cantidad'] for producto in inventario_dict])
        total_valor = sum([producto['precio'] * producto['cantidad'] for producto in inventario_dict])
        reporte = f'Reporte de la tienda {self.nombre}\n'
        reporte += f'Total de productos: {total_productos}\n'
        reporte += f'Total de cantidad: {total_cantidad}\n'
        reporte += f'Total de valor: ${total_valor:.2f}\n\n'
        for producto in inventario_dict:
            reporte += f'{producto["codigo"]}: {producto["nombre"]} - Precio: ${producto["precio"]:.2f} - Cantidad: {producto["cantidad"]}\n'
        return reporte
