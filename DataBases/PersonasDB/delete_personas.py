import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='xxxx', #insert host
    password='xxxxx', #insert password
    database='personas_db'
)

#execute UPDATE
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (7,) #with , otherwise error
cursor.execute(sentencia_sql, valores)
personas_db.commit() # guardar los cambios en la base de datos
print('Se ha eliminado la informacion')
cursor.close()
personas_db.close()