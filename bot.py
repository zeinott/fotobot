import discord
from discord.ext import commands
import json
import os

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATA_FILE = "photos.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@bot.command()
async def ekle(ctx, nickname):
    if not ctx.message.attachments:
        await ctx.send("Fotoğraf yükle.")
        return

    photo_url = ctx.message.attachments[0].url
    data = load_data()
    data[nickname.lower()] = photo_url
    save_data(data)

    await ctx.send(f"{nickname} kaydedildi.")

@bot.command()
async def bul(ctx, nickname):
    data = load_data()

    if nickname.lower() in data:
        await ctx.send(data[nickname.lower()])
    else:
        await ctx.send("Bulunamadı.")

bot.run(TOKEN)