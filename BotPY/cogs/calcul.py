import discord
from discord.ext import commands
from discord import app_commands
import typing

class Addition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="calcul", description="Calcul 2 nombres, fonctionne avec les addition, les soustraction, les multiplication et les divisions")
    async def calcul_slash(self, interaction: discord.Interaction, nombre1 : int, type:str, nombre2: int):
        if type not in ["+", "-", "*", "/"]:
            await interaction.response.send_message(f"Le type doit être [+,-,*,/], vous avez mis {type}", ephemeral=True)
            return

        if type == "+":
            result = nombre1 + nombre2
        elif type == "-":
            result = nombre1 - nombre2
        elif type == "*":
            result = nombre1 * nombre2
        elif type == "/":
            if nombre2 != 0:
                result = nombre1 / nombre2
            else:
                raise ValueError("La division par zéro n'est pas autorisée")
            
        await interaction.response.send_message(f"Le résultat de l'équation {nombre1} {type} {nombre2} est {result}", ephemeral=True)

    @calcul_slash.error
    async def say_error(self,interaction: discord.Interaction, error):
        await interaction.response.send_message("Tu n'as pas les permissions d'exécuter cette commande!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Addition(bot))
