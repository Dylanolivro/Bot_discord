import discord
from discord.ext import commands
from discord import app_commands
import datetime
import calendar
import time

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unban", description="Debannir un utilisateur")
    @app_commands.default_permissions(administrator=True)
    async def unban_slash(self, interaction: discord.Interaction, user_id: str, reason: str = None):
        user_id = int(user_id)
        banned_users = [ban async for ban in interaction.guild.bans()]
        user = None
        for ban in banned_users:
            if ban.user.id == user_id:
                user = ban.user
                break

        if user is None:
            await interaction.response.send_message(f"L'utilisateur avec l'ID {user_id} n'est pas dans la liste des bannis.", ephemeral=True)
            return

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
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Unban(bot))

