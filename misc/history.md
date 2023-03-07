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
- Connection from config.ini file using username, password, host and port given during the creation of the database.
- The use of the config.ini file allows us to work locally with this sensitive information without submitting it to github (using the .gitignore file).
- **INSERT** data to database. The database will register: prompt given to the ChatGPT API, the answer given, model used, date, temperature, max_tokens and status

# Deployment with docker
- Docker file creation included initialising with python 3.7.4, copying the gpt3app folder as well as the requirements.txt file.
- The OS is updated and the python libraries installed using pip and the requirements.txt.
- We then expose port 5000 to outside the docker container and launch the app.
- We also included ARG options in the docker file which then allow build-args being passed during `docker build`. This means that users will not have access to these login details but the app will still connect to the AWS RDS database.
- The build docker was pushed to dockerhub where it is available for use.

### build the docker image locally
`sudo docker build --build-arg DB_HOST=<db_host> --build-arg DB_PORT=3306 --build-arg DB_USERNAME=<username> --build-arg DB_PASSWORD=<password> --build-arg DB_DATABASE=<db_name> --tag gpt-app:v4 .`

### rename ready to go to seenstevo account
`sudo docker tag gpt-app:v4 seenstevo/:gpt-app:v4`

### upload the docker image to dockerhub
`sudo docker push seenstevo/gpt-app:v4`

### download it from dockerhub
`sudo docker pull seenstevo/gpt-app:v4`

### then to run the container
`sudo docker run -p 5000:5000 gpt-app:v4`

# Git Hub

[Repositorie](https://github.com/JNevado81/GPT3-App-Post-creator.git)

### upload commands
`git checkout dev`

`git pull`

`git checkout main`

`git merge dev`

- If there is a conflict, a git add and a git commit must be performed after the conflict is resolved.
---------
`git add .`

`git commit -m "xxxx"`

---------

`git push`
