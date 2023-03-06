import os
import configparser

# this config sets the AWS login values depending on if it is being run from the Docker image or as a local app

if os.environ.get('DB_HOST') != None:
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_database = os.environ.get('DB_DATABASE')
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_host = config['seandatabase']['host']
    db_port = config['seandatabase']['port']
    db_username = config['seandatabase']['username']
    db_password = config['seandatabase']['password']
    db_database = config['seandatabase']['database']