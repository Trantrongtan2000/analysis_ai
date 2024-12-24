from openai import OpenAI
import requests
from bs4 import BeautifulSoup

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
#messages=[]

def get_web_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  text_data = soup.get_text()
  print(text_data)
  return text_data

print("Welcome to the chatbot! Type 'exit' to quit.")
while True:
    #print(messages)
    user_input = input("You: ")
    if user_input == "exit":
        break
    if user_input == "search":
        url = 'https://www.google.com/search?q='+str(input("Enter the URL: "))
        user_input = get_web_data(url)
    response = client.chat.completions.create(
        model="gemma2",
        stream=True,
        messages=[{"role": "user", "content": user_input}]
    )
    #messages.append({"role": "user", "content": user_input})
    bot_reply = ''
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ''
    print(f"Bot: {bot_reply}")

# scrawl data from the web






