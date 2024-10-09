# main.py

from funciones import *



# Función principal para ejecutar el sistema
def sistema_inventario():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            cargar_producto()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            ordenar_inventario()
        elif opcion == '4':
            mostrar_producto_mas_caro()
        elif opcion == '5':
            mostrar_producto_mas_barato()
        elif opcion == '6':
            mostrar_productos_caros()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el sistema
sistema_inventario()
