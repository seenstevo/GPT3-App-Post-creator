# desarrollo del app.py.
- creacion de index.html
- static css stlye
- leccion de las entradas de usuario y logica para esegurarnos que tengamos todas
- llamada a la API de GPT
- preceso de la respuesta de GPT

# modules
- fetch_gpt_response()
- check_max_tokens()
- get_timestamp()
- establish_connection_aws()
- insert_row()
- inputs_non_empty()

# creacion de la base de datos
- cuenta de AWS
- creacion a partir de codigo
- conexion a partir de config.ini file
- INSERT datos a la base de datos

# despliegue con docker
- creacion de docker file
- ports
- docker build con build-args para AWS login
- push a dockerhub