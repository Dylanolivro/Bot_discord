import discord
from discord.ext import commands
from discord import app_commands

class BanList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="banlist", description="Liste des utilisateurs bannis")
    @app_commands.default_permissions(administrator=True)
    async def banlist_slash(self, interaction: discord.Interaction):
        banned_users = [ban async for ban in interaction.guild.bans()]
        if not banned_users:
            await interaction.response.send_message("Ce serveur n'a encore banni personne", ephemeral=True)
            return

        pretty_list = set()
        for ban in banned_users:
            user = ban.user
            bot_tag = "<:bottag:473742770671058964>" if user.bot else ""
            if user.discriminator == "0":
                data = f"•<@{user.id}> {user.name} {bot_tag} (ID: {user.id})"
            else:
                data = f"•<@{user.id}> {user.name} ({user.discriminator}) {bot_tag} (ID: {user.id})"
            pretty_list.add(data)

        await interaction.response.send_message("**Liste des bannis :** \n" + "\n".join(pretty_list), ephemeral=True)

    @banlist_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(BanList(bot))
