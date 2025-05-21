import requests
import os
from groq import Groq
# Get the API key from the environment variable or use the fallback value

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "Your_groq_key")
def query_llm(prompt):

# Get the API key from the environment variable or use the fallback value
   

# Initialize the Groq client with the API key
    client = Groq(api_key=GROQ_API_KEY)  # Pass the API key to the Groq constructor

# Add a message to the messages list
    messages = [{"role": "user", "content": prompt}]  # Example message

    completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=messages,  # Pass the messages list to the function
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=0.95,
    stream=True,
    stop=None,
    )

    for chunk in completion:
        return chunk.choices[0].delta.content 
       

