from flask import Flask, render_template, request
import os
import pandas as pd
import openai

dir_script = os.path.dirname(os.path.abspath(__file__))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder='app/templates')
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    prompt = request.form['prompt']
    
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1000,
    temperature=0.9
    )
    text_output = response.choices[0].text
    text_output = text_output.replace('\n', '<br>')
    text_output = text_output.replace('\t', '    ')
    return text_output + '<p><a href="/">Back</a></p>\n'

if __name__ == "__main__":
    app.run()