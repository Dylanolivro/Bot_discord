import discord
from discord.ext import commands
from discord import app_commands
import datetime
import calendar
import time

# ! FONCTIONNE MAIS AMELIORATION POUR QU'ON PUISSE DEBAN UN USER MAIS LONGTEMPS APRES

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unban", description="Debannir un utilisateur")
    @app_commands.default_permissions(administrator=True)
    async def unban_slash(self, interaction: discord.Interaction, user: discord.User, reason: str = None):
        if reason is None:
            reason = "Aucune raison fournie"
        ts = calendar.timegm(time.gmtime())
        channel = interaction.guild.get_channel(1169940364392681503)
        embed = discord.Embed(title="Debannisement", description="Un modérateur a débanni un utilisateur", color=0xff0000)
        embed.add_field(name="Information :", value=f"-> `Utilisateur` : {user.name}\n -> `Date` : <t:{ts}:R>\n->`Modérateur Responsable` : {interaction.user.mention}")
        embed.timestamp = datetime.datetime.now()

        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message(f"L'utilisateur {user.mention} a été débanni pour la raison suivante : {reason}", ephemeral=True)
        await channel.send(embed=embed)

    @unban_slash.error
    async def say_error(self,interaction: discord.Interaction, error):
        await interaction.response.send_message("Tu n'as pas les permissions d'exécuter cette commande!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Unban(bot))

