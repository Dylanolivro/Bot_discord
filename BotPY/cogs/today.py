import discord
from discord.ext import commands
from discord import app_commands
import datetime,time,calendar
import locale

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="today", description="Cette commande donne la date actuelle")
    @app_commands.default_permissions(administrator=True)
    async def today_slash(self, interaction: discord.Interaction):
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        date = datetime.datetime.today().strftime("%A %d %B %Y")
        await interaction.response.send_message(date, ephemeral=False)

    @today_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Test(bot))
