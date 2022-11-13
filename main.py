import redis
import requests
import json

db = 'localhost'
db_port = 6379


def voice_name_edit(channel_id, name) :
    r = redis.Redis(host=db, port=db_port, db=2)
    r.set(channel_id, name)


url = "https://vsza.hu/hacksense/status.json"
headers = {"User-Agent": "aRandomUserAgenttoMakeTheApiHappy"}
response = requests.get(url, headers=headers)
data = json.loads(response.content.decode('utf-8'))

cache = redis.Redis(host=db, port=db_port, db=3)


if (str(data['what']) != cache.get("hacksense").decode('utf-8')):
    state = str(data['what'])
    cache.set('hacksense', state )
    if data['what'] == True:
        voice_name_edit('998622942957150301','space-is-OPEN')
    else:
        voice_name_edit('998622942957150301','space-is-CLOSED')



# the channel edids pulled from db, by crow bot
#@tasks.loop(seconds=30)
#async def edit_vchannel_name():
#    r = redis.Redis(host=db, port=db_port, db=2)
#    for key in r.keys('*'):
#        cahnnel_id = key.decode("utf-8")
#        channel = client.get_channel(int(cahnnel_id))
#        await discord.VoiceChannel.edit(channel, name = r.getdel(key).decode("utf-8"))