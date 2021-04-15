import discord
import dataStorage
#585570690225274940-828815540533198879
message = "default message. Error has occurred."
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await send_message(message)
    print("test")
    await client.close()

async def send_message(message):
    user = await client.fetch_user(dataStorage.discordId)
    print(user)
    await user.send(message)

def start(m):
    global message
    message = m
    client.run("Nzk4Mjk2MDg4NTE5OTAxMTk1.X_y9Kw.PB6Ou5AJAR9YH9kRo5kZDqjkyB4")
