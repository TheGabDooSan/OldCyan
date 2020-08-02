import discord
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import *

import os
import asyncio
import random
import datetime


def bot_prefix(prefix = ':!'):
    return prefix

def randcolour():
    colours = [
        0xfecda5, 0xe7c4fc, 0x556edf,
        0x6e1faf, 0x303136
    ]

    return random.choice(colours)

async def error_embed(error_name = "Erreur", error = "Une erreur est survenue."):
    embed = discord.Embed(colour = discord.Colour.red())
    embed.add_field(name = "**Error** > {}".format(error_name), value = "<a:cross3:718861181653352536>  {}".format(error))
    embed.timestamp = datetime.datetime.utcnow()
    return embed

bot = commands.Bot(command_prefix = bot_prefix(), case_insensitive = True)
bot.remove_command('help')

memory = {"boss_pv": 70000000}

async def status_updater():
    time = 20
    while True:
        await bot.change_presence(
            activity = discord.Streaming(name = "🌸❦ EPHEDIA ❦🌸", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)
        guild = get(bot.guilds, id = 707063500903678023)
        await bot.change_presence(
            activity = discord.Streaming(name = f"{len(guild.members)} membres 🎇", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)
        await bot.change_presence(
            activity = discord.Streaming(name = "ma femme Kayla ❤️", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)
        await bot.change_presence(
            activity = discord.Streaming(name = "la Team Paillette 🎆", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)
        await bot.change_presence(
            activity = discord.Streaming(name = "@louana_kay ✏️", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)
        await bot.change_presence(
            activity = discord.Streaming(name = "Mon Tsukiiiiiiiiiiii 🌙", url = "https://www.twitch.tv/ephediafr")
        )
        await asyncio.sleep(time)


@bot.event
async def on_ready():
    print(
        f'''
            ------------------
            --->  [ ONLINE ]
            <{bot.user.id}>: {bot.user.name}
            ------------------
        '''
    )
    bot.loop.create_task(status_updater())


# Charger un fichier de ./cogs/{extension}
@bot.command()
async def load(ctx, extension):
    # Si celui qui a executé la commande n'est pas le développeur du Bot (ID: <@274558756522557440>)
    if ctx.message.author.id != 274558756522557440:
        await ctx.send(embed = await error_embed(
            error = "Vous devez être le développeur du bot pour executer cette commande."
        ))
    else:
        try:
            bot.load_extension('cogs.{}'.format(extension))
            embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Le module `{}.py` a bien été chargé.".format(extension)
            )
            await ctx.send(embed = embed)
        except ExtensionNotFound:
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionNotFound",
                error = "Le module `{}.py` n'a pas été trouvé.".format(extension)
            ))
        except ExtensionFailed:
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionFailed",
                error = "La fonction setup de cette extension a rencontré une erreur."
            ))
        except NoEntryPointError:
            await ctx.send(embed = await error_embed(
                error_name = "NoEntryPointError",
                error = "Cette extension n'a pas de fonction setup"
            ))
        except ExtensionAlreadyLoaded:
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionAlreadyLoaded",
                error = "Cette extension est déjà chargée"
            ))

# Recharger un fichier de ./cogs/{extension}
@bot.command()
async def reload(ctx, extension):
    # Si celui qui a executé la commande n'est pas le développeur du Bot (ID: <@274558756522557440>)
    if ctx.message.author.id != 274558756522557440:
        await ctx.send(embed = await error_embed(
            error = "Vous devez être le développeur du bot pour executer cette commande."
        ))
    else:
        try:
            bot.reload_extension('cogs.{}'.format(extension))
            embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Le module `{}.py` a bien été rechargé.".format(extension)
            )
            await ctx.send(embed = embed)
        except (ExtensionNotFound, ExtensionNotLoaded):
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionNotFound | ExtensionNotLoaded",
                error = "Le module `{}.py` n'existe pas ou n'a pas été chargé.".format(extension)
            ))
        except ExtensionFailed:
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionFailed",
                error = "L'extension `{}` a rencontrée une erreur, regardez la console.".format(extension)
            ))
        except NoEntryPointError:
            await ctx.send(embed = await error_embed(
                error_name = "NoEntryPointError",
                error = "Cette extension n'a pas de fonction setup."
            ))

# Décharger un fichier de ./cogs/{extension}
@bot.command()
async def unload(ctx, extension):
    # Si celui qui a executé la commande n'est pas le développeur du Bot (ID: <@274558756522557440>)
    if ctx.message.author.id != 274558756522557440:
        await ctx.send(embed = await error_embed(
            error = "Vous devez être le développeur du bot pour executer cette commande."
        ))
    else:
        try:
            bot.unload_extension('cogs.{}'.format(extension))
            embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Le module `{}.py` a bien été déchargé.".format(extension)
            )
            await ctx.send(embed = embed)
        except ExtensionNotLoaded:
            await ctx.send(embed = await error_embed(
                error_name = "ExtensionNotLoaded",
                error = "Le module `{}.py` n'a pas été chargé.".format(extension)
            ))


# Pour tous les fichiers dans ./cogs
for file_name in os.listdir('./cogs'):
    # Si le nom des fichiers se termine par ".py" et ne commence pas par "_"
    if file_name.endswith('.py') and not file_name.startswith('_'):
        # On charge les fichiers
        bot.load_extension('cogs.{}'.format(file_name[:-3]))


bot.run("NzE2NzU3Njg1NjU1MTc1Mjgx.XtQanA.ks29o3N3cvk2JgnxQjkqNJN_PEM")
