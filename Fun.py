import asyncio
import discord
import time
import datetime
from discord.ext import commands
from datetime import date


def __init__(self, bot):                                                                        #Define self,bot for class Main
        self.bot = bot

def __init__(self, message):
            self.requester = message.author
            self.channel = message.channel


class Fun:
    """Some usefull commands
    You can have some fun with them or get some research. 
    """
                                                                                                #What is write up here appears in the Area Help

    def __init__(self, bot):    
        self.bot = bot

        
    
    @commands.command(pass_context=True, no_pm=False)                                           #No_pm gives the choice to use the commands on PM
    async def hello(self, ctx):
        """Personalized message to everyone that bot knows"""
        userID = ctx.message.author.id
        if ctx.message.channel.id != "469480208878141470":                                      #IF the Channel ID is not this command do not work
            await self.bot.say("Cannot work in this channel <@%s>"%(userID))
            return False
        if ctx.message.author.id == "169546436797661185":                                       #User @UncleGrandpa
            await self.bot.say("<@%s> Hey Champ!!" %(userID))
        elif ctx.message.author.id == "199996704861323264":
            await self.bot.say("Olá <@%s> como vais? \nMeu querido Flexas!!!" %(userID))        #User @Fletcher
        elif ctx.message.author.id == "171013033970237440":
            await self.bot.say("Tudo em cima <@%s>, meu parceiro!!" %(userID))                  #User @rdnwiZard
        elif ctx.message.author.id == "169546810275135488":
            await self.bot.say("Se não é o javardinhas do <@%s> " %(userID))                    #User @Ghostlicht
        elif ctx.message.author.id == "169551808157450240":
            await self.bot.say(" <@%s>? És tu meu Korean Lover?" %(userID))                     #User @MC
        else:
            await self.bot.say("Por enquanto ainda só conheço alguns utilizadores")

    @commands.command(pass_context=True, no_pm=False)
    async def ping(self, ctx):
        """Test your Ping with Avô"""

        userID = ctx.message.author.id
        if (ctx.message.channel.id != "469480208878141470" and "423615623818510359"):
            await self.bot.say("Cannot work in this channel <@%s>"%(userID))
            return False
        else:
            await self.bot.say("<@%s> pong!" %(userID))

    @commands.command(pass_context=True, no_pm=False)
    async def fome(self, ctx):
        """If you are hungry!"""

        userID = ctx.message.author.id
        if (ctx.message.channel.id != "469480208878141470" and "423615623818510359"):
            await self.bot.say("Cannot work in this channel <@%s>"%(userID))
            return False
        else:
            await self.bot.say("<@%s> Estas com fome? \nToma lá uma :cookie: ^^" %(userID))

    @commands.command(pass_context=True, no_pm=False)
    async def dor(self, ctx):
        """Bot is not a doctor!"""

        userID = ctx.message.author.id
        if (ctx.message.channel.id != "469480208878141470" and "423615623818510359"):
            await self.bot.say("Cannot work in this channel <@%s>"%(userID))
            return False
        else:    
            await self.bot.say("<@%s> Pó crlh tu mais as tuas dores!\nJá estou cheio de te ouvir!" %(userID))

    @commands.command(pass_context=True, no_pm=False)
    async def time(self, ctx):
        """What time is it!?"""
        #In comment I have it in a hard way!!

        userID = ctx.message.author.id                                                          #Used to mention the User
        clock=datetime.datetime.now()
        #time=datetime.datetime.now().time()
        #data=date.today()
        #months=["January","February","March","April","May","June","July","August","September","OCtober","November","December"]
        #week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        if (ctx.message.channel.id != "469480208878141470" and "423615623818510359"):
            await self.bot.say("Cannot work in this channel <@%s>"%(userID))
            return False
        else:
            await self.bot.say("Here you go! <@%s>" %(userID))
            await self.bot.say(clock.strftime("Date: %A, %d %B %Y\nClock: %X"))
            #await bot.say("Date: %s" %(week[data.weekday()])+ ", %s" %(data.day) + " " +(months[data.month-1]) + " %s"  %(data.year)+
            #             "\nClock: %s" %(time.hour)+ ":%s"%(time.minute)+":%s"%(time.second))


def setup(bot):
    bot.add_cog(Fun(bot))
    print('Fun is loaded')
