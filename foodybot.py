# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pandas as pd
# from recipe import Recipe
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

columns = ['name', 'recipe']

@bot.command(name='foody')
async def suggestFood(ctx, *args):
    df = pd.read_csv('recipes.csv', index_col=0)

    if 'breakfast' in args:
        df = df[df['meal'].str.contains('B')]
    elif 'dinner' in args:
        df = df[df['meal'].str.contains('D')]
    elif 'lunch' in args:
        df = df[df['meal'].str.contains('L')]
    elif 'dessert' in args:
        df = df[df['meal'].str.contains('DE')]
    if 'vege' in args:
        df = df[df['vege'] == 1]
    if 'meat' in args:
        df = df[df['vege'] == 0]
    if 'fast' in args:
        df = df[df['fast'] == 1]

    data = df.sample()

    await ctx.send('``` {}```'.format('\n\n '.join((data[col]).to_string(index=False, header=False) for col in columns)))

bot.run(TOKEN)