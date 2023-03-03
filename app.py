from flask import Flask, render_template, request
import os
from app import models

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder = 'app/templates')
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # collect inputs from user once submit button pressed
    prompt = request.form['prompt']
    if prompt == "":
        return 'No prompt provided, please try again.' + '<p><a href="/">Back</a></p>\n'
    engine = request.form['engine'] # already has a default
    temperature = float(request.form['temperature'])    # needs a default
    max_tokens = int(float(request.form['max_tokens']))
    api_key = request.form['api_key']

    # send these to the gpt model
    text_output = models.fetch_gpt_response(prompt, api_key, engine, temperature, max_tokens)

    # process the output
    text_output = text_output.replace('\n', '<br>')
    text_output = text_output.replace('\t', '    ')
    return text_output + '<p><a href="/">Back</a></p>\n'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)