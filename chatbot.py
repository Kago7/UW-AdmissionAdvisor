import openai
from openai import OpenAI
import os
import prompt_formatter as pf

# API Key (set your API key with environment variable)
apikey=os.getenv('OPENAI_API_KEY')

# randomness level of responses (between 0 to 2, with 2 being more random)
randomness_level = 0.4

# asks user to choose a major
major = input("Enter Major You're Interested In: ")

# handles the opening message
def opening():
    # gets initial prompt
    initial_prompt = pf.get_prompt(major)

    # NEW opening message
    client = OpenAI(api_key=apikey)    
       
    completion = client.chat.completions.create(model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": initial_prompt}])
    
    # print(completion.choices[0].text)
    
      
    # OLD opening message
    # completion = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    # messages=[{"role": "user", "content": initial_prompt}],
    # presence_penalty=0,
    # frequency_penalty=0,
    # temperature=randomness_level           # handles the "randomness" of responses
    # )

    response = completion.choices[0].message.content
    
    
    
    print(response)


# handles asking user for their question and outputting response
def ask_and_response(question):
    prompt = pf.formatq(major, question)

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
    )

    response = completion.choices[0].message.content
    print(response)



opening()
while True:
    print("\n-------------------\n")

    # asks user to enter their question
    question = input("Please Enter Your Question: ")

    # exits program if user input is "exit"
    if question == "exit":
        break

    ask_and_response(question)