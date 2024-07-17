import discord
import os
from dotenv import load_dotenv
load_dotenv()

import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    json_data = json.loads(response.text)
    return json_data['slip']['advice']

def get_affirmation():
    response = requests.get('https://www.affirmations.dev/')
    json_data = json.loads(response.text)
    return json_data['affirmation']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self,message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content.startswith('$advice'):
            await message.channel.send(get_advice())
        elif message.content.startswith('$quote'):
            await message.channel.send(get_affirmation())
        else:
            await message.channel.send('Wrong command! Maybe try $meme or $advice or $quote')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
token = os.getenv('BOT_PROJECT_API_KEY')
client.run(token)