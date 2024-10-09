INVENTARIO = []

# Función que devuelve el precio del producto
def obtener_precio(producto):
    return producto[1]

# Función para cargar productos al inventario
def cargar_producto():
    n = int(input("¿Cuántos productos deseas agregar?: "))
    for _ in range(n):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        INVENTARIO.append([nombre, precio, cantidad])
    print(f"{n} producto(s) agregado(s) al inventario.")

# Función para buscar un producto por nombre
def buscar_producto():
    if not INVENTARIO:
        print("No hay productos en el inventario.")
        return
    nombre = input("Ingresa el nombre del producto a buscar: ").lower()
    encontrado = False
    for producto in INVENTARIO:
        if producto[0].lower() == nombre:
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print(f"Producto '{nombre}' no encontrado.")

# Función para ordenar el inventario por precio ascendente
def ordenar_inventario():
    if not INVENTARIO:
        print("No hay productos en el inventario.")
        return
    INVENTARIO.sort(key=obtener_precio)  # Usamos la función obtener_precio
    print("Inventario ordenado por precio: ")
    for producto in INVENTARIO:
        print(producto)

# Función para mostrar el producto más caro
def mostrar_producto_mas_caro():
    if not INVENTARIO:
        print("No hay productos en el inventario.")
        return
    producto_mas_caro = max(INVENTARIO, key=obtener_precio)  # Usamos la función obtener_precio
    print(f"Producto más caro: {producto_mas_caro}")

# Función para mostrar el producto más barato
def mostrar_producto_mas_barato():
    if not INVENTARIO:
        print("No hay productos en el inventario.")
        return
    producto_mas_barato = min(INVENTARIO, key=obtener_precio)  # Usamos la función obtener_precio
    print(f"Producto más barato: {producto_mas_barato}")

# Función para mostrar productos con precio mayor a 15000
def mostrar_productos_caros():
    if not INVENTARIO:
        print("No hay productos en el inventario.")
        return
    productos_caros = [p for p in INVENTARIO if p[1] > 15000]
    if productos_caros:
        print("Productos con precio mayor a 15000: ")
        for producto in productos_caros:
            print(producto)
    else:
        print("No hay productos con precio mayor a 15000.")
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Cargar producto/s")
    print("2. Buscar producto")
    print("3. Ordenar inventario")
    print("4. Mostrar producto más caro")
    print("5. Mostrar producto más barato")
    print("6. Mostrar productos con precio mayor a 15000")
    print("7. Salir")