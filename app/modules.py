import openai
from datetime import datetime
import pymysql
import configparser


def fetch_gpt_response(prompt: str, api_key: str, engine: str, temperature: float, max_tokens: int) -> str:
    '''
    Function wrapper to call gpt3 model with prompt.

    Args:
        prompt (str): the input to the GPT3 model
        api_key (str): API key of user to allow access to GPT3 API
        engine (str): the GPT3 model to use
        temperature (float): a value between 0 and 1 which influences the creativity of the GPT3 model
        max_tokens (int): the max tokens that the model will use which defines the max length of the output

    Returns:
        str: the status of the call, success or error
        str: the response text

    '''
    # this will only be nessesary if we use one of our keys as a default
    # if api_key == "":
    #     config = configparser.ConfigParser()
    #     config.read('./app/config.ini')
    #     openai.api_key = config['gpt3_api_key']['api_key']
    # else:
    #     openai.api_key = api_key
    openai.api_key = api_key

    try:
        output = openai.Completion.create(
        engine = engine,
        prompt = prompt, 
        max_tokens = max_tokens,
        temperature = temperature
    )

        return "Success", output.choices[0].text
    except:
        return "Error", "Something went wrong with the GPT3 call. Please check API key and try again. Do you still have tokens?"




def get_timestamp() -> str:
    '''
    Simply returns a string of the current time and date to log a query 
    '''
    date_time_query = datetime.now()
    return date_time_query.strftime("%d/%m/%Y %H:%M:%S")



def establish_connection_aws():
    '''
    Function wrapper establish the connection to the AWS SQL database
    Reads in the connection information from the config.ini file
    Used in the insert_row function

    Returns:
        a database connection
    '''

    config = configparser.ConfigParser()
    config.read('./app/config.ini')

    db = pymysql.connect(host = config['seandatabase']['host'],
                         user = config['seandatabase']['username'],
                         password = config['seandatabase']['password'],
                         port = int(config['seandatabase']['port']),
                         database = config['seandatabase']['database'],
                         cursorclass = pymysql.cursors.DictCursor)
    
    return db


def insert_row(prompt: str, response: str, date: str, engine: str, temperature: float, max_tokens: int, gpt_call_status: str) -> None:
    '''
    Function to insert into the SQL database the log of each call
    Use the establish_connection_aws() function to establish the database connection

    Args:
        prompt (str): the input to the GPT3 model
        response (str): the response from GPT3
        api_key (str): API key of user to allow access to GPT3 API
        engine (str): the GPT3 model to use
        temperature (float): a value between 0 and 1 which influences the creativity of the GPT3 model
        max_tokens (int): the max tokens that the model will use which defines the max length of the output

    Returns:
        None
    '''

    db = establish_connection_aws()

    cursor = db.cursor()

    insert_data = '''
    INSERT INTO respuestas (preguntas, respuestas, fecha, engine, temperature, max_tokens, gpt_call_status)
    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
    ''' % (prompt, response, date, engine, temperature, max_tokens, gpt_call_status)

    cursor.execute(insert_data)
    db.commit()
    db.close()


def inputs_non_empty(prompt, api_key, temperature, max_tokens):
    '''
    Helper function to check that inputs have been input before making a call to GPT3
    '''
    if (prompt == "" or api_key == "" or temperature == "" or max_tokens == ""):
        return False
    else:
        return True