class Tienda:
    def __init__(self, id, inventario, ventas, productos, cal_prod):
        self.id_tienda = id
        self.cal_prod = cal_prod
        self.inventario = inventario
        self.ventas = ventas
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, venta):
        self.ventas.append(venta)

    def abastecer_producto(self, id_producto, cantidad):
        for producto in self.productos:
            if producto.id == id_producto:
                producto.cant_actual += cantidad
                break

    def cambiar_producto(self, id_producto, nombre, tipo, cant_minima, precio_unitario):
        for producto in self.productos:
            if producto.id == id_producto:
                producto.nombre = nombre
                producto.tipo = tipo
                producto.cant_minima = cant_minima
                producto.precio_unitario = precio_unitario
                break

    def calcular_total_ventas(self):
        total_ventas = 0
        for venta in self.ventas:
            total_ventas += venta.total_venta
        return total_ventas

    def obtener_producto_mas_vendido(self):
        producto_mas_vendido = None
        max_cantidad_vendida = 0
        for producto in self.productos:
            cantidad_vendida = sum(detalle.total_prod for detalle in producto.detalle)
            if cantidad_vendida > max_cantidad_vendida:
                producto_mas_vendido = producto
                max_cantidad_vendida = cantidad_vendida
        return producto_mas_vendido

    def obtener_producto_menos_vendido(self):
        producto_menos_vendido = id
        min_cantidad_vendida = float('inf')
        for producto in self.productos:
            cantidad_vendida = sum(detalle.total_prod for detalle in producto.detalle)
            if cantidad_vendida < min_cantidad_vendida:
                producto_menos_vendido = producto
                min_cantidad_vendida = cantidad_vendida
        return producto_menos_vendido

    def calcular_total_dinero_ventas(self):
        return sum(venta.total_venta for venta in self.ventas)

    def calcular_dinero_promedio_por_unidad(self):
        total_unidades = sum(venta.total_prod for venta in self.ventas)
        total_dinero = sum(venta.total_venta for venta in self.ventas)
        if total_unidades > 0:
            dinero_promedio = total_dinero / total_unidades
            return dinero_promedio
        else:
            return 0.0
class Producto:
    def __init__(self, id, nombre, tipo, cant_actual, cant_minima, precio_unitario):
        self.id = id
        self.tipo = tipo
        self.nombre = nombre
        self.cant_actual = cant_actual
        self.cant_minima = cant_minima
        self.precio_unitario = precio_unitario
        self.detalle = []

    def agregar_detalle(self, detalle):
        self.detalle.append(detalle)

    def calcular_precio_total(self):
        return self.cant_actual * self.precio_unitario
class DetalleVenta:
    def __init__(self, id, total_venta, total_prod):
        self.id = id
        self.total_venta = total_venta
        self.total_prod = total_prod
def mostrar_menu():
    print("1. Agregar producto a la tienda")
    print("2. Realizar una venta")
    print("3. Abastecer la tienda con un producto")
    print("4. Cambiar un producto")
    print("5. Visualizar información de los productos")
    print("6. Calcular estadísticas de ventas")
    print("7. Salir")
    print()
productos = []
ventas = []
tienda = Tienda("Mi Tienda", [], ventas, productos, "Ejemplo")
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        # Agregar producto a la tienda
        id_producto = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        tipo = input("Ingrese el tipo del producto: ")
        cant_actual = int(input("Ingrese la cantidad actual del producto: "))
        cant_minima = int(input("Ingrese la cantidad mínima del producto: "))
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        producto = Producto(id_producto, nombre, tipo, cant_actual, cant_minima, precio_unitario)
        productos.append(producto)
        tienda.agregar_producto(producto)
        print("Producto agregado exitosamente.")
    elif opcion == "2":
        # Realizar una venta
        id_venta = input("Ingrese el ID de la venta: ")
        total_venta = float(input("Ingrese el monto total de la venta: "))
        total_prod = int(input("Ingrese la cantidad total de productos vendidos: "))
        detalle = DetalleVenta(id_venta, total_venta, total_prod)
        ventas.append(detalle)
        producto_id = input("Ingrese el ID del producto vendido: ")
        for producto in productos:
            if producto.id == producto_id:
                producto.agregar_detalle(detalle)
                producto.cant_actual -= total_prod
                break
        print("Venta registrada exitosamente.")
    elif opcion == "3":
        # Abastecer la tienda con un producto
        id_producto = input("Ingrese el ID del producto: ")
        cantidad = int(input("Ingrese la cantidad a abastecer: "))

        tienda.abastecer_producto(id_producto, cantidad)
        print("La tienda ha sido abastecida con éxito.")
    elif opcion == "4":
        # Cambiar un producto
        id_producto = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        tipo = input("Ingrese el nuevo tipo del producto: ")
        cant_minima = int(input("Ingrese la nueva cantidad mínima del producto: "))
        precio_unitario = float(input("Ingrese el nuevo precio unitario del producto: "))

        tienda.cambiar_producto(id_producto, nombre, tipo, cant_minima, precio_unitario)
        print("Producto cambiado exitosamente.")
    elif opcion == "5":
        print("Información de los productos:")
        for producto in productos:
            print("ID:", producto.id)
            print("Nombre:", producto.nombre)
            print("Tipo:", producto.tipo)
            print("Cantidad actual:", producto.cant_actual)
            print("Cantidad mínima:", producto.cant_minima)
            print("Precio unitario:", producto.precio_unitario)
            print()
    elif opcion == "6":
        producto_mas_vendido = tienda.obtener_producto_mas_vendido()
        producto_menos_vendido = tienda.obtener_producto_menos_vendido()
        total_ventas = tienda.calcular_total_ventas()
        dinero_promedio = tienda.calcular_dinero_promedio_por_unidad()

        print("Estadísticas de ventas:")
        print("Producto más vendido:")
        print("ID:", producto_mas_vendido.id)
        print("Nombre:", producto_mas_vendido.nombre)
        print("Tipo:", producto_mas_vendido.tipo)
        print()

        print("Producto menos vendido:")
        print("ID:", producto_menos_vendido.id)
        print("Nombre:", producto_menos_vendido.nombre)
        print("Tipo:", producto_menos_vendido.tipo)
        print()

        print("Total de dinero obtenido por ventas:", total_ventas)
        print("Dinero promedio obtenido por unidad de producto vendida:", dinero_promedio)
        print()

    elif opcion == "7":
        print("fin del programa!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
