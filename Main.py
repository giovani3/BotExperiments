import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from flask import Flask, render_template, request
#from weatherUpdate import WeatherUpdate
import time
import datetime
import asyncio
import requests


startup_extensions = ["Fun","Weather","Music"]
bot = commands.Bot("?")



@bot.event #On_ready defines what is going to appear when bot gets Ready
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Type ?help"),status=discord.Status("dnd"))

time=datetime.datetime.now()
print(time.strftime("%d-%B-%Y %X"))
print("Bot is online and connected to Discord!")


class Main_commands():
        def __init__(self, bot):
            self.bot = bot
            
        def __init__(self, message):
            self.requester = message.author
            self.channel = message.channel

#Check if the Extensions were loaded or not! IF not, then why!
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print ('Failed to load extension {}\n{}'.format(extension, exc))


bot.run("NDY4NzkxODk0ODgxNzMwNTcw.DjIZvA.iN0ruLuhOku9N_BGV8JizOty_a4")
