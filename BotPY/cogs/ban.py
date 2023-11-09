import discord
from discord.ext import commands
from discord import app_commands
import datetime,time,calendar

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Bannir un utilisateur")
    @app_commands.default_permissions(administrator=True)
    async def ban_slash(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        if reason is None:
            reason = "Aucune raison fournie"
            
        ts = calendar.timegm(time.gmtime())
        channel = interaction.guild.get_channel(1169940364392681503)
        await interaction.guild.ban(user, reason=reason)
        embed = discord.Embed(title="Bannisement", description="Un modérateur a banni un utilisateur", color=0xff0000)
        embed.add_field(name="Information :", value=f"-> `Utilisateur` : {user.mention}\n -> `Date` : <t:{ts}:R>\n->`Modérateur Responsable` : {interaction.user.mention}\n ->`Raison` : \n```{reason}```")
        embed.timestamp = datetime.datetime.now()

        await interaction.response.send_message(f"L'utilisateur {user.mention} a été banni pour la raison suivante : {reason}", ephemeral=True)
        await channel.send(embed=embed)

    @ban_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Ban(bot))
