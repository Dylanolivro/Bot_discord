import discord
from discord.ext import commands
from discord import app_commands
import requests
import json

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="joke", description="Affiche une blague aléatoire")
    async def joke_slash(self, interaction: discord.Interaction):
        response = requests.get('https://v2.jokeapi.dev/joke/Any?lang=fr')
        joke = json.loads(response.text)
        if joke['type'] == 'single':
            await interaction.response.send_message(joke['joke'], ephemeral=False)
        else:
            await interaction.response.send_message(joke['setup'] + "\n" + joke['delivery'], ephemeral=False)
    
    @joke_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Joke(bot))
