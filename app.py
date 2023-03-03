from flask import Flask, render_template, request
import os
from app import modules

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder = 'app/templates')
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def my_form_post():
    # get timestamp
    time_stamp_query = modules.get_timestamp()
    # collect inputs from user once submit button pressed
    prompt = request.form['prompt']
    if prompt == "":
        return 'No prompt provided, please try again.' + '<p><a href="/">Back</a></p>\n'
    engine = request.form['engine']
    temperature = float(request.form['temperature'])
    max_tokens = int(float(request.form['max_tokens']))
    api_key = request.form['api_key']
    if api_key == "":
        return 'No OpenAI API key provided, please try again.' + '<p><a href="/">Back</a></p>\n'

    # send these to the gpt model
    text_output = modules.fetch_gpt_response(prompt, api_key, engine, temperature, max_tokens)

    # process the output
    text_output_html = text_output.replace('\n', '<br>')
    text_output_html = text_output_html.replace('\t', '    ')

    modules.insert_row(prompt, text_output, time_stamp_query)

    
    return text_output_html + '<p><a href="/">Back</a></p>\n'


@app.route('/', methods = ['POST'])
def log_app_use():
    pass

if __name__ == "__main__":
    app.run(host = 'localhost', port = 5000)