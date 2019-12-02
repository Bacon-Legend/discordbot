import discord
import random

import json

client = discord.Client()

@client.event
async def on_ready():
    print("Bacon Is Ready To Be Served")

@client.event
async def on_message(message):
    author = str(message.author)[:-5]
    
    spamats = "@" +str(author) + " "
    SPAMaats = spamats * 10
    if message.author == client.user:
        return
    if not message.content.startswith("&"):
        return
    if "&hello" in message.content.lower():
        rand = random.randint(1,3)
        if rand == 1:
            await message.channel.send("Hello There, How are you doing, " +str(author) +"?") 
        if rand == 2:
            await message.channel.send("Whats up " +str(author) +"?") 
        if rand == 3:
            await message.channel.send("How are you doing today, " +str(author) +"?") 
    if "&pewdiepie" in message.content.lower():
        await message.channel.send("lasagna")
    if "&bacon" in message.content.lower():
        await message.channel.send("https://d1q0twczwkl2ie.cloudfront.net/wp-content/uploads/2015/06/bacon.jpg")
    if "&bacon2" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/649470331358281751/649473813393965116/bacon22.jpg")
    if "&mike" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/649470331358281751/649476805937332234/mike.jpg")
    if "&lenny" in message.content.lower():
        face = random.randint(1,5)
        if face == 1:
            await message.channel.send("┐(￣ヘ￣)┌")
        elif face == 2:
            message.channel.send("¯\_(ツ)_/¯")
        elif face == 3:
            await message.channel.send("┻━┻ ︵ ¯\_( ͡° ͜ʖ ͡°)_/¯ ︵ ┻━┻")
        elif face == 4:
            await message.channel.send("(┛ಠ_ಠ)┛彡┻━┻")
        elif face == 5:
            await message.channel.send("( う-´)づ︻╦̵̵̿╤── \(˚☐˚”)/")
    if "&random" in message.content.lower():
        rand = random.randint(1,10)
        await message.channel.send(rand)
    if "&spam" in message.content.lower():
        await message.channel.send(SPAMaats)
    return 
TOKEN = "NjQ5NDY4MTQ5MzU1MzgwNzQ3.XeB5ig.AycIkAEEhX7izRmpUdEaNbb3jKE"
client.run("NjQ5NDY4MTQ5MzU1MzgwNzQ3.XeB-qA.nzO6oPIfSJLOufRCrGlAPDXL0UM")