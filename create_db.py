#libraries
import pymysql




username = "admin"
password = "TheBridgeSchool"
host = "database-2.cvuovpb4vssk.us-east-2.rds.amazonaws.com" 
port = 3306


db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor
)

# El objeto cursor es el que ejecutará las queries y devolverá los resultados

cursor = db.cursor()


#Create database

create_db = '''CREATE DATABASE respuestas_GPT'''
cursor.execute(create_db)

#Select database and create table

cursor.connection.commit()
use_db = ''' USE respuestas_GPT'''
cursor.execute(use_db)

create_table = '''
CREATE TABLE respuestas (
    id INT NOT NULL auto_increment,
    preguntas TEXT,
    respuestas TEXT,
    fecha TEXT,
    primary key (id)
)
'''
cursor.execute(create_table)
db.commit()
db.close()