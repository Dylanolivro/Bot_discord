import discord
from discord.ext import commands
from discord import app_commands

class Calcul(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def convert_to_int_if_possible(value):
        try:
            if value.is_integer():
                return int(value)
            else:
                return value
        except Exception as e:
            print(e)

    @app_commands.command(name="calcul", description="Calcul 2 nombres, addition, soustraction, multiplication et divisions")
    async def calcul_slash(self, interaction: discord.Interaction, nombre1 : float, type:str, nombre2: float):
        if type not in ["+", "-", "*", "/"]:
            await interaction.response.send_message(f"Le type doit être [+,-,*,/], vous avez mis {type}", ephemeral=False)
            return
        
        nombre1 = self.convert_to_int_if_possible(nombre1)
        nombre2 = self.convert_to_int_if_possible(nombre2)

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
                await interaction.response.send_message(f"La **division par zéro** n'est pas autorisée.\nVotre calcul : [ {nombre1} {type} {nombre2} ]", ephemeral=False)
                return
            
        result = round(result,3)
        await interaction.response.send_message(f"Le résultat de l'équation [ {nombre1} {type} {nombre2} ] est : {result}", ephemeral=False)

    @calcul_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Calcul(bot))
