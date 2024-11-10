from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
APP_KEY = os.getenv("APP_KEY")

print("En que puedo ayudarte hoy?")

pregunta = input()

history = [{
                "role": "system", #Behavior orders
                "content": "Sos un profesor de colegio secundario en Argentina. Sos extrovertído y te gusta enseñar."
            # },
            # {
            #     "role": "assistant", #Behavior context given by previous answers
            #     "content": "Chicos que alegria verlos, ¿En qué puedo ayudarlos hoy?" 
            # },
            # {
            #     "role": "user", #Behavior context given by the question of the user
            #     "content": pregunta
            }]

while pregunta.lower() != "salir":

    history.append({"role": "user", "content": pregunta})

    client = OpenAI(
        api_key=APP_KEY
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )

    print(completion.choices[0].message.content)

    history.append({"role": "assistant", "content": completion.choices[0].message.content})

    pregunta = input()

print("Chat terminado.")
