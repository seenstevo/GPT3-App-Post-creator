import openai
from datetime import datetime
import pymysql


def fetch_gpt_response(prompt, api_key, engine, temperature, max_tokens):

    if api_key == "":
        openai.api_key = open("./app/gpt_api_key.txt", "r").read()
    else:
        openai.api_key = api_key

    output = openai.Completion.create(
        engine = engine,
        prompt = prompt, 
        max_tokens = max_tokens,
        temperature = temperature
    )

    return output.choices[0].text


def get_timestamp():
    date_time_query = datetime.now()
    return date_time_query.strftime("%d/%m/%Y %H:%M:%S")


def establish_connection_aws():
    username = "admin"
    password = "TheBridgeSchool"
    host = "database-2.cvuovpb4vssk.us-east-2.rds.amazonaws.com" 
    port = 3306

    db = pymysql.connect(host = host,
                         user = username,
                         password = password,
                         cursorclass = pymysql.cursors.DictCursor,
                         port = port)
    
    return db


def insert_row(prompt, response, date):

    db = establish_connection_aws()

    cursor = db.cursor()

    use_db = ''' USE respuestas_GPT'''

    cursor.execute(use_db)

    insert_data = '''
    INSERT INTO respuestas (preguntas,respuestas,fecha)
    VALUES ('%s', '%s', '%s')
    ''' % (prompt, response, date)

    cursor.execute(insert_data)
    db.commit()
    db.close()