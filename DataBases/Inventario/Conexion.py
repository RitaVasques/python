from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'inventario_db'
    USERNAME = 'xxxxxxx' #introduce username
    PASSWORD = 'xxxxxxxxxx' # Introduce Password
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'inventario_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Error obtencion de pool: {e}')
        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def free_connection(cls, conexion):
        conexion.close()
