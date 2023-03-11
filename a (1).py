from ast import Await, If
from asyncio import constants
from cgitb import text
from email import message
from email.mime import image
from gettext import install
from lib2to3.pgen2.token import AWAIT
from logging import _STYLES
import math
from modulefinder import Module
from msilib.schema import File
from multiprocessing import context
from multiprocessing.connection import Client
from multiprocessing.sharedctypes import Value
from pydoc import cli, describe
from pyexpat.errors import messages
from random import Random, random
from socket import if_indextoname
from statistics import variance
from tkinter import Button
from tkinter.tix import IMAGE
from tkinter.ttk import Style
from turtle import color, title
from types import MemberDescriptorType
from unicodedata import name
from urllib import response
import discord
import asyncio
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from tkinter.tix import IMAGE
import urllib.request, json 
import urllib, json

client = commands.Bot(command_prefix=',')

token = "OTgzNzc0Mjk1NjQ3OTk3OTgy.GZ-n0g.a5jLc7FIqR1Yp4QELhQLiuau0SaD9h8YBuedZQ"
curseWord = ['мам', 'tata82','хохол','бля','хуй','блять','хуйлуша','соси','член','жопа','еблан','пидр','негр','ебать','даун','долбоеб','еблан','пидор','пизда']

@client.listen('on_message')
async def ай(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} На этом сервера запрещены маты, не матерись пожалуйста")
    else:
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы ДЕБИЛ```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Вы не имеете права```")


@client.event
async def on_ready():
    print("Старт")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ip: dreammc.su"))
    DiscordComponents(bot, change_discord_methods=True)


@client.command()
async def сайт(ctx):
    embed = discord.Embed(
        title="Нажми для перехода :)",
         color=0xf1c40f,
        description="Ссылка для перехода на DreamMC",
        url='https://dreammc.ru/',
    )
    await ctx.send(embed=embed)


@client.command()
async def повтори(ctx, *, arg):
    await ctx.send(arg)
    


@client.command()
async def ip(ctx):
    embed = discord.Embed(
        title="Айпи DreamMC\nIP dreammc.su ( прокси)",
    )
    await ctx.send(embed=embed)


@client.command()
async def голос(ctx):
    embed = discord.Embed(
        title="Отдать свой голос ☻",
        description="Ссылка для перехода на minecraftrating",
        url='https://minecraftrating.ru/vote/83916/',
    )
    await ctx.send(embed=embed)


@client.command()
async def бан(ctx):
    embed = discord.Embed(
        title="Бан-лист ☻",
        color=0x992d22,
        description="Список забаненых игроков на DreamMC",
        url='https://dreammc.ru/banlist/',
    )
    await ctx.send(embed=embed)@client.command()


@client.command()
async def бб(ctx):
    embed = discord.Embed(
        title="Доброй ночи DreamMC ♡",
        color=0xf1c40f,
    )
    await ctx.send(embed=embed)
    

import random
import discord
from discord.ext import commands

config = {
    'token': 'your-token',
    'prefix': ',',
}

bot = commands.Bot(command_prefix=config['prefix'])

@client.command()
async def число_до_10(ctx, *arg):
    await ctx.reply(random.randint(0, 10))


config = {
    'token': 'your-token',
    'prefix': ',',
}

bot = commands.Bot(command_prefix=config['prefix'])

@client.command()
async def число_до_50(ctx, *arg):
    await ctx.reply(random.randint(0, 50))


config = {
    'token': 'your-token',
    'prefix': ',',
}

bot = commands.Bot(command_prefix=config['prefix'])

@client.command()
async def число_до_100(ctx, *arg):
    await ctx.reply(random.randint(0, 100))


config = {
    'token': 'your-token',
    'prefix': ',',
}

bot = commands.Bot(command_prefix=config['prefix'])

@client.command()
async def число_до_0(ctx, *arg):
    await ctx.reply(random.randint(-100, 0))


@client.command()
async def карта(ctx):
    embed = discord.Embed(
        title="Карта DreamMC",
        color=3066993,
        description="Карта сервера DreamMC",
        url='https://dynmap.dreammc.ru/#world;surface;-7,64,-7;0',
    )
    await ctx.send(embed=embed)


@client.command()
async def ВК(ctx):
    embed = discord.Embed(
        title="ВК DreamMC",
        color=3066993,
        description="ВК сервера DreamMC",
        url='https://vk.com/vanilladl',
    )
    await ctx.send(embed=embed)


@client.command()
async def сервер(ctx):
    embed = discord.Embed(
        title="DreamMC",
        color=15418782,
        description="Средний онлайн            **7**\nЗабанено игроков         **225**\nПоставлено блоков    **997 563**\nСломано блоков       **512 473**\nВерсия                  **1.19**\nДанные обновляються каждую неделю\nПоследнее обновление **23.06.2022**",
        url='https://dreammc.ru/',
    )
    await ctx.send(embed=embed)


config = {
    'token': 'your-token',
    'prefix': ',',
}

bot = commands.Bot(command_prefix=config['prefix'])

@client.command()
async def сброс(ctx, *arg):
    await ctx.reply('Нарушения были сброшены')


@client.command()
async def собака(ctx):
    await ctx.send("https://i.sunhome.ru/dreamer/133/govoryashhaya-sobaka-v2.xxl.jpg")


@client.command()
async def кот(ctx):
    await ctx.send("https://i.yapx.cc/QPdAn.jpg")


@client.command()
async def мем(ctx):
    await ctx.send("https://pp.userapi.com/FmFt-98YqtOOG8e2TBCMVPQEVT6IIIJOPeK6aw/jbrWR6IUEKY.jpg")



@client.command()
async def Бан_лист_1(ctx, *arg):
    embed = discord.Embed(
        title=" :cookie: Бан-лист DreamMC",
        color=3066993,
        description="**Страница 1 из 1**\n**1** KoT_PiLoT\n**2** Wetr1ng\n**3** mr_maksim\n**4** Frede_Mojang\n**5** JoeBiden\n**6** Levan0\n**7** Za_haRch_ik735\n**8** hatr3d\n**9** Hikirius\n**10** qmniks\n\n\nВаш запрос",
        jsonStr = '{"one" : "1", "two" : "2", "three" : "3"}'
    )
    await ctx.reply(embed=embed)



@client.command()
async def тест(ctx):
    embed = discord.Embed(
        title=" :trophy: Конкурс на новый спавн ",
        color=3066993,
        description="**Здравствуйте, дорогие игроки. В связи с последними событиями мы объявляем конкурс на лучшую постройку спавна для сервера DreamMC.**\n\n**При победе вы получите ⚒ **\n\nВсе ваши работы вы можете отправить в <#922906663139287070> с #спавн\n\n **Требования:**\n`1. Должна быть возможность строить в выживании.`\n`2. Размер 50-75 блоков от центра.( В каждую сторону 50-75 блоков )`\n`3. Подходить под ландшафт.`\n`3.1 Ландшафт не должен быть плоским.`\n`4. Иметь более 3 дорог.`\n`5. Стойка объявлений (2 шт.)`\n`6. Средневековый стиль.`\n`7. Центр открытый (5-7 блоков от центра)`\n`8. Должна быть ферма для новичков. (Еды)`\n`9. Портал в ад (оформленный адекватно)`\nТакже можете уточнять пункты у <@254607149248806914>",
    )
    await ctx.send(embed=embed)


@client.command()
async def button(ctx):
    embed = discord.Embed(
        title="**Информация о сервере**",
        color=15158332,
        description="** ``` 📕・Основная информация: ``` ** \n<#912000940230467614> - вход на сервер\n<#952153120467730513> - информация о сервере\n<#907517610931929089> - новости сервера\n<#943939583782051841> - пожертвования серверу\n<#1084054851236933693> -  связь с администрацией сервера\n\n**```💬・Основные чаты:```**\n <#768447361553924099> - общение\n<#912008847844073504> - команды ботов\n<#922906663139287070> - скриншоты из разных игр\n<#945316070531661825> - торговля\n\n**```🔊・Голосовые каналы:```**\n <#912318244499640340> - создать свой голосовой канал\n<#916725424787173417> - резервный канал\n<#994275751312502885> - канал администрации\n\n**```🚨・Роли персонала:```**\n<@&912022107456667729> - администрация сервера\n\n **```🩰・Основные роли:```**\n<@&912410979655102566> - элита сервера \n <@&912000577305714749> - участник сервера\n <@&984019822620844042> - грифер сервера\n <@&912548420739301426> - бот сервера",
    )

    await ctx.send(embed=embed,  components=[[Button(style=ButtonStyle.URL, label="Сайт", url="https://dreammc.su"), Button(style=ButtonStyle.URL,  label="Проголосовать", url="https://minecraftrating.ru/vote/83916")]])



    

@client.command()
async def butto(ctx):
    embed = discord.Embed(
    embed.set_image(url="https://media.discordapp.net/attachments/922906663139287070/1084018198850060298/image.png?width=1202&height=676")
    )
    await ctx.send(embed=embed)
 



@client.command()
async def тестик(ctx):
    embed = discord.Embed(
        title="Информация о сервере",
        color=57731,
        description="** ``` 📕・Основная информация: ``` ** \n<#912000940230467614> - вход на сервер\n<#952153120467730513> - информация о сервере\n<#907517610931929089> - новости сервера\n<#943939583782051841> - пожертвования серверу\n<#1084054851236933693> -  связь с администрацией сервера\n\n**```💬・Основные чаты:```**\n <#768447361553924099> - общение\n<#912008847844073504> - команды ботов\n<#922906663139287070> - скриншоты из разных игр\n<#1079274386588180621> - жалобы на игроков\n<#945316070531661825> - торговля\n\n**```🔊・Голосовые каналы:```**\n <#912318244499640340> - создать свой голосовой канал\n<#916725424787173417> - резервный канал\n<#994275751312502885> - канал администрации\n\n**```🚨・Роли персонала:```**\n<@&912022107456667729> - администрация сервера\n\n **```🩰・Основные роли:```**\n<@&912410979655102566> - элита сервера \n <@&912000577305714749> - участник сервера\n <@&984019822620844042> - грифер сервера\n <@&912548420739301426> - бот сервера",
    )
    await ctx.send(embed=embed)



client.run(token);   



