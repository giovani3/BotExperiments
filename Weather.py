import asyncio
import discord
from discord.ext import commands
from weatherUpdate import WeatherUpdate

def __init__(self, bot):                                                                        #Define self,bot for class Main
        self.bot = bot

def __init__(self, message):
            self.requester = message.author
            self.channel = message.channel

class Weather:
    """Weather related commands.
    Works in multiple servers at once.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def weather(self, ctx):
        """Search the Weather!! Em Construção!"""

        weather = WeatherUpdate("2d3dd7deab4e55ed3caf555d225d9f3f")
        result=None
        chatMessage = ctx.message.content.lower().split()

        try:
                if chatMessage[0]=="hello":
                    result = "hello! I am weather bot :) type !commands for my functionality!"


                elif chatMessage[0] == "commands":

                    result = "Command1: !temperature\nCommand2: !weather\nCommand3: !weatherdetail\nCommand4: !humidity\nCommand5: !windspeed\n\nMore specific search: Dublin,ie etc"


                elif chatMessage[0]=="weather":

                    result = weather.getWeatherStatus(chatMessage[1])


                elif chatMessage[0]=="weatherdetail":

                    result = weather.getWeatherStatusDetail(chatMessage[1])


                elif chatMessage[0]=="temperature":

                    result = weather.getTemperature(chatMessage[1])


                elif chatMessage[0]=="humidity":

                    result = weather.getHumidity(chatMessage[1])


                elif chatMessage[0]=="windspeed":

                    result = weather.getWindSpeed(chatMessage[1])


                elif chatMessage[0]=="cloudcoverage":

                    result = weather.getCloudCoverage(chatMessage[1])

                if result: #checking against invalid command
                    await bot.say(result)

        except ValueError as invalid:

            await bot.say(invalid)

def setup(bot):
    bot.add_cog(Weather(bot))
    print('Weather is loaded')
