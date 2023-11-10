import os
from dotenv import load_dotenv
import mysql.connector
import threading
import time


load_dotenv()

class Config():

    CHANNEL_LOGS_BAN_UNBAN = 1169940364392681503
    CHANNEL_MESSAGE_AUTO = 1172534258271784963

    DB_CONFIG = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "test_fk"
        }
    
    @staticmethod
    def get_token():
        return os.getenv('DISCORD_TOKEN')
    
    @staticmethod
    async def load_extensions(bot):
        for filename in os.listdir("BotPY\cogs"):
            if filename.endswith(".py"):
                if filename[:-3] not in ['view']:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Cogs <{filename[:-3]}> bien chargé")

    def connect():
        return mysql.connector.connect(**Config.DB_CONFIG)

    def insert(connection,name,password):
        params= (name,password)
        sql = """INSERT INTO user(name,password) VALUES(%s,%s)"""
        connection.cursor().execute(sql,params)


class DatabaseChecker(threading.Thread):
    def __init__(self, bot, channel_id):
        threading.Thread.__init__(self)
        self.bot = bot
        self.channel_id = channel_id
        self.last_checked_id = self.get_last_user_id()

    def get_last_user_id(self):
        connection = Config.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) FROM user")
        return cursor.fetchone()[0]

    def run(self):
        while True:
            connection = Config.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, password FROM user WHERE id > %s", (self.last_checked_id,))
            results = cursor.fetchall()
            for result in results:
                self.last_checked_id = result[0]
                self.bot.loop.create_task(self.send_message(result[1], result[2]))
            time.sleep(10)  # Check every 10 seconds

    async def send_message(self, user_name, user_password):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(f"Un nouvel utilisateur a été ajouté à la base de données. Nom d'utilisateur : {user_name}, Mot de passe : {user_password}")
