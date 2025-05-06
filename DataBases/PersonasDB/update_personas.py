import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='xxxx', #insert host
    password='xxxxx', #insert password
    database='personas_db'
)

#execute UPDATE
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Flores', 45, 7)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # guardar los cambios en la base de datos
print('Se ha modificado la informacion')
cursor.close()
personas_db.close()