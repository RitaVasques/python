from gestion_inventario import GestionInventario
from Producto import Producto

print('*** Gestion de Inventario ***')
option = None

while option != 6:
    print(f'''Menu:
    1. Mostrar Productos
    2. Agregar Producto
    3. Buscar Producto
    4. Actualizar Producto
    5. Eliminar Producto
    6. Salir''')
    opcion = int(input('Escribe tu opción (1-6): '))
    if opcion == 1:
        productos = GestionInventario.seleccionar()
        if productos:
            print('\n*** Listado de Productos ***')
            for producto in productos:
                print(producto)
        else:
            print('No hay productos en inventario')
    elif opcion == 2:
        existe = False
        nombre_new = input('Escribe el nombre: ')
        productos = GestionInventario.seleccionar()
        for producto in productos:
            if producto.nombre.lower() == nombre_new.lower():
                existe = True
        if existe == False:
            cantidad_new = input('Escribe la cantidad: ')
            precio_new = input('Escribe el precio: ')
            categoria_new = input('Escribe la categoria: ')
            producto_new = Producto(nombre_new, cantidad_new, precio_new, categoria_new)
            producto_added = GestionInventario.agregar(producto_new)
            print(f'{producto_added} nuevo producto {nombre_new}')
        else:
            print('Producto ya existe')
    elif opcion == 3:
        existe = False
        nombre_new = input('Escribe el nombre: ')
        productos = GestionInventario.seleccionar()
        for producto in productos:
            if producto.nombre.lower() == nombre_new.lower():
                existe = True
                print(producto)
        if existe == False:
            print('producto no encontrado')
    elif opcion == 4:
        existe = False
        nombre_new = input('Escribe el nombre: ')
        productos = GestionInventario.seleccionar()
        for producto in productos:
            if producto.nombre.lower() == nombre_new.lower():
                existe = True
        if existe == True:
            cantidad_new = input('Escribe la cantidad: ')
            precio_new = input('Escribe el precio: ')
            producto_new = Producto(nombre_new, cantidad_new, precio_new)
            producto_act = GestionInventario.actualizar(producto_new)
            print(f'{producto_act} ha sido actualizado - {nombre_new}')
        else:
            print('Producto no encontrado, no se puede actualizar')
    elif opcion == 5:
        existe = False
        nombre_new = input('Escribe el nombre del producto a eliminar: ')
        productos = GestionInventario.seleccionar()
        for producto in productos:
            if producto.nombre.lower() == nombre_new.lower():
                existe = True
        if existe == True:
            producto_eliminar = Producto(nombre_new,)
            producto_clear = GestionInventario.eliminar(producto_eliminar)
            print(f'{producto_clear} eliminado - {nombre_new}')
        else:
            print('Producto a eliminar no encontrado')
    else:
        print('Saliendo del sistema...')
        break
               
    