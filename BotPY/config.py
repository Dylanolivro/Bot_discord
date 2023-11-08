import os
from dotenv import load_dotenv

class Config():

    CHANNEL_LOGS_BAN_UNBAN = 1169940364392681503

    @staticmethod
    def get_token():
        load_dotenv()
        return os.getenv('DISCORD_TOKEN')
    
    @staticmethod
    async def load_extensions(bot):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                if filename[:-3] not in ['view']:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Cogs <{filename[:-3]}> bien chargé")