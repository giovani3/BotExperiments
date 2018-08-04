import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from flask import Flask, render_template, request
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

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Bot is online and connected to Discord!")

    #channel = bot.get_channel('474986185295527957')
    #await bot.join_voice_channel(channel)
    #print('Bot joined the channel.')


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


bot.run("")
