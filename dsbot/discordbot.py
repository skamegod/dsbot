import discord
from discord.ext import commands
import yt_dlp

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к мацанию титек")

@bot.command()
async def hello(ctx):
    await ctx.send(f"АСАЛАМАЛЕЙКУМ {ctx.author.mention}!!!!")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"ПОДКЛЮЧИЛСЯ К ДИДЖЕЙСКОЙ УСТАНОВКЕ {channel}")
    else:
        await ctx.send("ТЫ НЕ В ВОИСЕ ДУРАК")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("ПОКИНУЛ ДИДЖЕЙСКУЮ УСТАНОВКУ")
    else:
        await ctx.send("МЕНЯ ТУТ НЕТУ ТАКТО")

@bot.command()
async def play(ctx, url: str):
    voice_client = ctx.voice_client

    if not voice_client:
        await ctx.send("МЕНЯ ТУТ НЕТУ ТАКТО")
        return
    
    if voice_client.is_playing():
        voice_client.stop()

    FFMPEG_OPTIONS = {'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['url']

    source = discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
    voice_client.play(source)
    await ctx.send(f"ФИГАРЮ ЭТО: **{info['title']}**")

bot.run("TOKEN")