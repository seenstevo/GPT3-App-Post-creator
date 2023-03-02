from flask import Flask, render_template, request
import os
import pandas as pd
import openai

dir_script = os.path.dirname(os.path.abspath(__file__))
#app para comunicar con chatgp3 y database en AWS



os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = render_template(dir_script + '\\app\\templates\\index.html')
    return template

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

app.run()