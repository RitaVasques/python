from Producto import Producto
from Conexion import Conexion

class GestionInventario:
    SELECCIONAR = 'SELECT * FROM invetario ORDER BY nombre'
    INSERTAR = 'INSERT INTO invetario(nombre, cantidad, precio, categoria) VALUES(%s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE invetario SET cantidad=%s, precio=%s WHERE nombre=%s'
    ELIMINAR = 'DELETE FROM invetario WHERE nombre=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f'Error al seleccionar producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.free_connection(conexion)
    
    @classmethod
    def agregar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al insertar producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.free_connection(conexion)

    @classmethod
    def actualizar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.cantidad, producto.precio, producto.nombre)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al actualizar producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.free_connection(conexion)

    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al eliminar producto: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.free_connection(conexion)
