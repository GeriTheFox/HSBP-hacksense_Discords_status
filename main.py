from discord.ext import tasks
import discord
import requests
import json
from decouple import config



class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_background_task.start()

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

    @tasks.loop(seconds=60)
    async def my_background_task(self):
        channel = client.get_channel(config('CHANNEL_ID'))
        url = "https://vsza.hu/hacksense/status.json"
        headers = {"User-Agent": "aRandomUserAgenttoMakeTheApiHappy"}
        response = requests.get(url, headers=headers)
        data = json.loads(response.content.decode('utf-8'))
        #print(data)
        if data['what'] == True:
            await discord.VoiceChannel.edit(channel, name = 'space-is-OPEN')
        else:
            await discord.VoiceChannel.edit(channel, name = 'space-is-CLOSED')


    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

client = MyClient()

client.run(config('DISCORD_TOKEN'))

