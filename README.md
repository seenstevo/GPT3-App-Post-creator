# Automatic Post Generator using ChatGPT

This project creates a Flask web application using in Python that allows users to flexibly interact with various GPT3 models. The final project consists of the development and deployment of the application as a docker image which can be run locally on any machine. The user interactions are stored using Amazon Web Services (RDS).

## Objectives
* Develop a web application using Python and Flask that connects to the GPT3 API to generate responses to user prompts. 
* The front-end should be simple but usable for the user.
* Store the questions, answers, and corresponding dates in a database deployed on the cloud (AWS).
* Deploy the application in Docker.

## Technologies Used
* Python
* Flask
* GPT3 API
* AWS RDS
* Docker

## Deployment with Docker
<<<<<<< HEAD
<<<<<<< HEAD

1. Load the image by running `docker pull seenstevo/gpt-app`
2. Run the image: `docker run -p 5000:5000 <id_image>`
  (You can see image id by running `docker images` in your terminal)
3. Click on the first http adress shown in your terminal. It should usually be: http://127.0.0.1:5000
     
=======
=======
>>>>>>> e73aca1ea214b53f44656b0e4ba133f2654a3c44
1. Ensure you have docker installed on your machine.
2. Load the image by running `docker pull seenstevo/gpt-app:v3`
3. Run the image ensuring to set the ports: `docker run -p 5000:5000 seenstevo/gpt-app:v3`
  (You can see image id by running `docker images` in your terminal)
4. Click on the first http address shown in your terminal. It should usually be: http://127.0.0.1:5000
5. Ensure you have a valid API key from OpenAI to use.
6. Select your GPT3 model. See [here](https://platform.openai.com/docs/models/gpt-3-5) for more information on their capabilities.
7. Set the max tokens value to define the max combined length of your input text as well as GPT3's response. If you input over the max allowed per model, the max will be used.
8. Setting the temperature between 0 (conservative, low creativity) and 1 (unhinged, creative) will influence the models behaviour.
9. Once you've written your prompt, hit the submit (Enviar datos) button to get your GPT3 response.
10. If there are no errors with the call, you will see the response from GPT3. Otherwise you will see the error message "Something went wrong with the GPT3 call...".
<<<<<<< HEAD
>>>>>>> dev
=======
>>>>>>> e73aca1ea214b53f44656b0e4ba133f2654a3c44

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## Contributors
[seenstevo](https://github.com/seenstevo)

[JNevado81](https://github.com/JNevado81)

[JaredR33](https://github.com/JaredR33)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
