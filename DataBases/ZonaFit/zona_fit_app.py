from Cliente_DAO import ClienteDAO
from Cliente import Cliente

print('*** Clientes Zona Fit (GYM) ***')
opcion = None

while opcion != 5:
    print(f'''Menu:
    1. Listar Clientes
    2. Agregar Cliente
    3. Modificar Cliente
    4. Eliminar Cliente
    5. Salir''')
    opcion = int(input('Escribe tu opción (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre_new = input('Introduce el nombre: ')
        apellido_new = input('Introduce el apellido: ')
        membresia_new = input('Introduce la membresia: ')
        cliente1 = Cliente(nombre=nombre_new, apellido=apellido_new, membresia=membresia_new)
        clientes_insertados = ClienteDAO.insertar(cliente1)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3:
        id_mod = input('Introduce el id del cliente a modificar: ')
        nombre_new = input('Introduce el nombre: ')
        apellido_new = input('Introduce el apellido: ')
        membresia_new = input('Introduce la membresia: ')
        cliente1 = Cliente(id_mod, nombre_new, apellido_new, membresia_new)
        clientes_modificados = ClienteDAO.actualizar(cliente1)
        print(f'Clientes modificados: {clientes_modificados}')
    elif opcion == 4:
        id_mod = input('Introduce el id del cliente a eliminar: ')
        cliente1 = Cliente(id_mod,)
        clientes_eliminados = ClienteDAO.eliminar(cliente1)
        print(f'Clientes eliminados: {clientes_eliminados}')
    else:
        print('Salimos de la app...')
        
