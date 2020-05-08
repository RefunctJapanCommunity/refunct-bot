import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「!c」で始まるか調べる
    if message.content.startswith("!c"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send("The race will begin in 10 seconds!")
            time.sleep(5)
            await message.channel.send("The race will begin in 5 seconds!")
            time.sleep(2)
            await message.channel.send("3")
            time.sleep(1)
            await message.channel.send("2")
            time.sleep(1)
            await message.channel.send("1")
            time.sleep(1)
            await message.channel.send("Go!")

client.run("NzA4MjYwNzk1Mjg0MTkzMzAx.XrUxbg.kEV7_Z77XWLVVyovXTM4Mr250FM")