import discord
from discord.ext import commands
from discord import app_commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed_reactions = ["👍", "👎", "🤷"]
        self.poll_message_id = None  # Ajoutez cette ligne

    @app_commands.command(name="poll", description="Crée un sondage")
    async def poll_slash(self, interaction: discord.Interaction, *, question: str):
        await interaction.response.defer(ephemeral=False)
        message = await interaction.followup.send(question, ephemeral=False)
        for emoji in self.allowed_reactions:
            await message.add_reaction(emoji)
        self.poll_message_id = message.id  # Ajoutez cette ligne

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user != self.bot.user and reaction.message.id == self.poll_message_id:  # Modifiez cette ligne
            if str(reaction.emoji) in self.allowed_reactions:
                for emoji in self.allowed_reactions:
                    if str(reaction.emoji) != emoji:
                        await reaction.message.remove_reaction(emoji, user)
            else:
                await reaction.remove(user)
            
    @poll_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if isinstance(error, commands.CheckFailure):
            await interaction.response.send_message("Tu n'as pas les permissions !", ephemeral=True)
        else:
            await interaction.response.send_message(f"Une erreur s'est produite : {error}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Poll(bot))
