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
    engine = request.form['engine']
    temperature = request.form['temperature']
    max_tokens = request.form['max_tokens']
    api_key = request.form['api_key']

    if modules.inputs_non_empty(prompt, api_key, temperature, max_tokens):
        temperature = float(temperature)
        max_tokens = int(float(max_tokens))

        # send these to the gpt model
        # seria util saber si hay un error con la respuesta con GPT y hacemos un try, except o algo
        gpt_call_status, text_output = modules.fetch_gpt_response(prompt, api_key, engine, temperature, max_tokens)

        # process the output
        text_output_html = text_output.replace('\n', '<br>')
        text_output_html = text_output_html.replace('\t', '    ')

        modules.insert_row(prompt, text_output, time_stamp_query, engine, temperature, max_tokens, gpt_call_status)
        
        return text_output_html + '<p><a href="/">Back</a></p>\n'
    
    else:
        return 'Inputs missing, please try again.' + '<p><a href="/">Back</a></p>\n'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)