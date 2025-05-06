import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='xxxx', #insert host
    password='xxxxx', #insert password
    database='personas_db'
)

#execute INSERT
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Victor', 'Ramos', 46)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # guardar los cambios en la base de datos
print(f'Se ha agregado el nuevo registro: {valores}')
cursor.close()
personas_db.close()