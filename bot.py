import os
import discord
from dotenv import load_dotenv


class devClient(discord.Client):
    





if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    client.run(token)