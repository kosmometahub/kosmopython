import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

#response = openai.Completion.create(model="text-davinci-003", prompt="What are the best places to visit in LA", temperature=0, max_tokens=7)
response = openai.Completion.create(model="text-davinci-003", prompt="What are the best places to visit in LA")
#print(response.choices[0]['text'])
print(response)
