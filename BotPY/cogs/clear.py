import discord
from discord.ext import commands
from discord import app_commands

class ClearChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Supprime tous les messages d'un canal ou un nombre spécifique de ceux-ci.")
    @commands.has_permissions(manage_messages=True)
    async def clear_slash(self, interaction: discord.Interaction, number: int = None):
        if number is None:
            await interaction.response.send_message("Tous les messages ont été effacés.", ephemeral=True)
            await interaction.channel.purge()
        else:
            await interaction.response.send_message(f"{number} messages ont été effacés.", ephemeral=True)
            await interaction.channel.purge(limit=number)

    @clear_slash.error
    async def clear_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ClearChannel(bot))
