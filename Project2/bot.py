import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (   
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    gacha_results = [
        'Saber: Artoria Pendragon',
        'Archer: EMIYA',
        'Lancer: Cu Cuhllain',
        'Rider: Medusa',
        'Assassin: Sasaki Kojiro',
        'Caster: Medea of Colchis',
        'Berserker: Heracles',
        'Avenger: Angra Mainyu',
     ]

    if message.content == 'Summon!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(gacha_results)
        await message.channel.send(response)

client.run(TOKEN)
