import openai



def fetch_gpt_response(prompt, api_key, engine, temperature, max_tokens):

    if api_key == "":
        openai.api_key = open("./app/gpt_api_key.txt", "r").read()
    else:
        openai.api_key = api_key

    output = openai.Completion.create(
        engine = engine,
        prompt = prompt, 
        max_tokens = max_tokens,
        temperature = temperature
    )

    return output.choices[0].text