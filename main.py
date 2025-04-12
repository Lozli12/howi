
import discord
from discord.ext import commands
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

bot_active = False

@bot.command()
async def startman(ctx):
    global bot_active
    bot_active = True
    await ctx.send("✅ Бот активирован. Теперь он будет реагировать на события.")

@bot.event
async def on_message(message):
    global bot_active
    if message.author == bot.user:
        return

    if not bot_active:
        return

    if message.content.lower().startswith("ping"):
        await message.channel.send("pong")

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"✅ Бот запущен как {bot.user}")

bot.run(DISCORD_TOKEN)
