import discord
from discord import app_commands
from discord.ext import commands
from config import Config
from config import DatabaseChecker

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="?",intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
token = Config.get_token()

@bot.event
async def on_ready():

    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)

    await Config.load_extensions(bot)

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

    checker = DatabaseChecker(bot, Config.CHANNEL_MESSAGE_AUTO)
    checker.start()

bot.run(token)