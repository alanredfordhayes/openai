import os
import openai
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser(
    prog = 'Logo Maker',
    description = 'A program that creates logos using openai',
    epilog = 'Generate api key at openai.com'
)

parser.add_argument('-p', '--prompt') 
args = parser.parse_args()

def open_ai_image_create(prompt, n, size):
    response = openai.Image.create(prompt=prompt, n=n, size=size)
    image_url = response['data'][0]['url']
    return image_url

image_url = open_ai_image_create(
    prompt = args.prompt,
    n=1,
    size="1024x1024"
)

print(image_url) 