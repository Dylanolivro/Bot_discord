import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Affiche toutes les commandes du bot")
    async def help_slash(self, interaction: discord.Interaction):
        commands = [f"/{command.name} - {command.description}" for command in self.bot.commands]
        
        print(commands)

        await interaction.response.send_message("\n".join(commands), ephemeral=False)


    @help_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Help(bot))
