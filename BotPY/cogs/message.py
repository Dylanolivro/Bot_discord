import discord
from discord.ext import commands
from discord import app_commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @staticmethod
    def str_format(messageContent,word):
        return messageContent.lower().rstrip(' ?.!').endswith(word)

    @commands.Cog.listener()
    async def on_message(self,message):
        
        if message.content.lower().rstrip(' ?.!').endswith("ping"):
            await message.channel.send("Pong !")

        if message.content.lower().rstrip(' ?.!').endswith("quoi"):
            await message.channel.send("Feur !")            

async def setup(bot):
    await bot.add_cog(Message(bot))