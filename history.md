# Development of the app.py
- Creation of index.html: web page where we can launch the questions to Chat-GPT.
- Creation of the style sheet (cascading style sheets): design and presentation of the web page.
- Web parameters: 
    - prompt: text input, question. 
    - engine: engine to generate the answer.
    - max_tokens: limits the number of tokens the model can generate. 
    - api_key: API key for authentication.
    - temperature: degree of freedom we give to the model when generating the answer, the higher the number, the greater the creative freedom.
- Validation of the parameters entered by the user on the web. Mandatory: prompt, api_key and max_tokens. Checks the max_tokens value against the chosen model.
- GPT API call (request).
- GPT response.

# Functions
- fetch_gpt_response(): function wrapper to call gpt3 model with prompt. Will also call max_tokens function to ensure no values out of range 
are passed.
- check_max_tokens(): this function will check the given max_tokens value against the max allowed for a given model and limit this value
- get_timestamp(): simply returns a string of the current time and date to log a query
- establish_connection_aws(): function wrapper establish the connection to the AWS SQL database. Reads in the connection information from the config.py file. Used in the insert_row function.
- insert_row(): function to insert into the SQL database the log of each call. Use the establish_connection_aws() function to establish the database connection.
- inputs_non_empty(): helper function to check that inputs have been input before making a call to GPT3.

# Creation of the database
- AWS account
- Creation of the database using Amazon RDS
- Change security group, inbound rules to allow connection from python using pymysql library
- Connection from config.ini file using username, password, host and port given during the creation of the database
- **INSERT** data to database. The database will register: prompt given to the ChatGPT API, the answer given, model used, date, temperature, max_tokens and status

# Deployment with docker
- Docker file creation
- Ports
- Docker build con build-args para AWS login
- Push a dockerhub
