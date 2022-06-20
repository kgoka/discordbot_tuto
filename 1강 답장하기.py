import discord
client = discord.Client()
token = "TOKEN"

@client.event
async def on_message(message):
    if message.content == "안녕?":
        await message.channel.send("안녕!", reference=message)

client.run(token)
