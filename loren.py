import nextcord
import json
import random
from requests.sessions import InvalidSchema
from datetime import datetime
from pymongo import MongoClient
from nextcord.ext import commands
from validators.utils import ValidationFailure
from nextcord import Interaction, message_command, slash_command, user_command, SlashOption

with open('settings.json', 'r') as json_file:
  settings = json.load(json_file)




#loghcnl = settingssub.find({"_id": 5})
#for logch in loghcnl:
#    logchannel = (logch['logchannel'])

class loren(commands.Cog):
    """Filters words of moderators choice"""

    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        # Now let's check if the sender is a bot in general, if so also don't process the command either
        if message.author.bot == True:
            return
        if not message.guild:
            return await message.channel.send("k")
        newid = random.randint(1,40)
        chs = int(newid)
        if chs == 5:
            await message.channel.send("k")

def setup(client):
    client.add_cog(loren(client))
