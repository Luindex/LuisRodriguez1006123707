# main.py
import sys
productos = []

def crear_producto():
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        productos.append({"nombre": nombre, "precio": precio})
        print("Producto agregado correctamente.")
    except ValueError:
        print("Precio inválido. Intente nuevamente.")

def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        for i, prod in enumerate(productos):
            print(f"{i+1}. {prod['nombre']} - ${prod['precio']:.2f}")
        print(f"Total de productos: {len(productos)}")

def actualizar_producto():
    listar_productos()
    try:
        index = int(input("Número del producto a actualizar: ")) - 1
        if 0 <= index < len(productos):
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))
            productos[index] = {"nombre": nombre, "precio": precio}
            print("Producto actualizado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_producto():
    listar_productos()
    try:
        index = int(input("Número del producto a eliminar: ")) - 1
        if 0 <= index < len(productos):
            productos.pop(index)
            print("Producto eliminado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def mostrar_menu():
    print("\n=== SISTEMA CRUD DE PRODUCTOS v1.0 ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    if sys.stdin.isatty():
        main()
    else:
        print("Entorno no interactivo detectado. Saltando ejecución del menú.")