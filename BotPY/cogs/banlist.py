import discord
from discord.ext import commands
from discord import app_commands

# ! NE FONCTIONNE PAS 

class BanList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="banlist", description="Liste des utilisateurs bannis")
    @app_commands.default_permissions(administrator=True)
    async def banlist_slash(self, interaction: discord.Interaction):
        banned_users = await interaction.guild.bans()
        if not banned_users:
            await interaction.response.send_message("Ce serveur n'a encore banni personne", ephemeral=True)
            return

        userid = [user.id for user in banned_users]
        name = [user.name for user in banned_users]
        discriminator = [user.discriminator for user in banned_users]
        bot = [user.bot for user in banned_users]

        newlist = []
        for item in bot:
            if item:
                item = "<:bottag:473742770671058964>"
            else:
                item = ""
            newlist.append(item)
        bot = newlist

        total = list(zip(userid, name, discriminator, bot))

        pretty_list = set()
        for details in total:
            data = "•<@{}>{} ({}#{}) ".format(details[0], details[3], details[1], details[2])
            pretty_list.add(data)

        await interaction.response.send_message("**Liste des bannis :** \n{}".format("\n".join(pretty_list)), ephemeral=True)

    @banlist_slash.error
    async def say_error(self,interaction: discord.Interaction, error):
        await interaction.response.send_message("Tu n'as pas les permissions d'exécuter cette commande!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(BanList(bot))
