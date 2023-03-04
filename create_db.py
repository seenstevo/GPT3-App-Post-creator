#libraries
import pymysql
import configparser

config = configparser.ConfigParser()
config.read('./app/config.ini')


db = pymysql.connect(host = config['seandatabase']['host'],
                     user = config['seandatabase']['username'],
                     password = config['seandatabase']['password'],
                     port = int(config['seandatabase']['port']),
                     cursorclass = pymysql.cursors.DictCursor)

cursor = db.cursor()

#Create database
create_db = '''CREATE DATABASE respuestas_GPT'''
cursor.execute(create_db)
cursor.connection.commit()

#Select database and create table
use_db = ''' USE respuestas_GPT'''
cursor.execute(use_db)

create_table = '''
CREATE TABLE respuestas (
    id INT NOT NULL auto_increment,
    preguntas TEXT,
    respuestas TEXT,
    fecha TEXT,
    engine TEXT,
    temperature FLOAT,
    max_tokens INT,
    gpt_call_status TEXT,
    primary key (id)
)
'''
cursor.execute(create_table)
db.commit()
db.close()