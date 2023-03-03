import openai
import time
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
    return time.time


def establish_connection_aws():
    username = "admin"
    password = "adminjjs"
    host = "database-1.ccl50gywe0s6.us-east-2.rds.amazonaws.com" 
    port = 3306

    db = pymysql.connect(host = host,
                         user = username,
                         password = password,
                         cursorclass = pymysql.cursors.DictCursor,
                         port = port)
    
    return db


def insert_row(prompt, response, date, table):

    db = establish_connection_aws()

    cursor = db.cursor()

    insert_data = '''
    INSERT INTO %s (preguntas, respuestas, fecha)
    VALUES ('%s', '%s', '%s')
    ''' % (table, prompt, response, date)

    cursor.execute(insert_data)
    db.commit()
    db.close()
