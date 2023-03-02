import openai

try:
    openai.api_key = open("gpt_api_key.txt", "r").read()
except:
    print("No gpt_api_key.txt in the directory with your credentials")


def fetch_gpt_response(prompt, engine = "text-davinci-002", temperature = 0.9):


    output = openai.Completion.create(
        engine = engine,
        prompt = prompt, 
        max_tokens = 3900,
        temperature = temperature
    )


    return output.choices[0].text