import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from main import randcolour, error_embed

import random
import asyncio
import urllib
import base64
from datetime import datetime
from random import randint, randrange, choice

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def randdigit(self, mini = 1, maxi = 999):
        return f"{randrange(mini, maxi):03}"

    embed_thumb = {"embed": None}

    @commands.command(aliases = ['edit-bot'])
    async def edit_bot(self, ctx, param: str, *, value: str):
        if ctx.author.id == 707402860853329931 or ctx.author.id == 274558756522557440:
            param = param.lower()
            try:
                if param == "username" or param == "name":
                    await self.bot.user.edit(
                        username = value
                    )
                    await ctx.send(f"Username du bot changé en : `{value}`")
                elif param == "avatar" or param == "icon" or param == "icone":
                    with urllib.request.urlopen(value) as response:
                        image = response.read()
                    await self.bot.user.edit(
                        avatar = image
                    )
                    await ctx.send(f"Avatar du bot changé en : \n`{value}`")
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Vous devez entrer un paramètre valide. (`username` / `avatar`)"
                    ))
            except discord.HTTPException as e:
                await ctx.send(embed = await error_embed(
                    error_name = "HTTPException",
                    error = e
                ))
            except discord.InvalidArgument as e:
                await ctx.send(embed = await error_embed(
                    error_name = "InvalidArgument",
                    error = e
                ))

    @commands.command(aliases=['create_embed', 'embedmsg', 'msgembed'])
    @has_permissions(administrator=True)
    async def embed(self, ctx, *, message):

        embed = discord.Embed(
            colour = randcolour(),
            description = message
        )
        embed.set_footer(
            text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.", 
            icon_url = "https://cdn.discordapp.com/emojis/711639609808781374.png"
        )
        if self.embed_thumb["embed"] is not None:
            embed.set_thumbnail(url = self.embed_thumb["embed"])

        await ctx.message.delete()
        await ctx.send(embed = embed)
    
    @commands.command(aliases=['embed_thumb', 'embed-image'])
    async def embed_image(self, ctx, url: str):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            if url == "reset":
                self.embed_thumb["embed"] = None
                embed = discord.Embed(
                    colour = randcolour(),
                    description = "Le thumbnail a été reset."
                )
            else:
                self.embed_thumb["embed"] = url
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"__Nouveau thumbnail__ : [link]({url})"
                )
            await ctx.message.delete()
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))
    
    @commands.command(aliases=['ver', 'vers'])
    async def version(self, ctx):
        botuser = self.bot.user
        embed = discord.Embed(
            title = "Bot Infos - Version",
            description = "Informations sur le développement du bot.\n"
                          "Libraries : [Python3.7](https://www.python.org/downloads/release/python-370/) - [discord.py](https://github.com/Rapptz/discord.py)",
            colour = randcolour()
        )
        embed.add_field(name = "Projet",
                        value = "Fondatrice FantasyGroupe | Ephédia-Game : <@707402860853329931>\n"
                                "Développeur | Game Master : <@274558756522557440>",
                        inline = False)
        embed.add_field(name = "BotUser",
                        value = f"{botuser.mention} ({botuser.name}#{botuser.discriminator})",
                        inline = False)

        await ctx.send(embed = embed)
    
    @commands.command(aliases=['purge', 'clean'])
    @has_permissions(administrator=True)
    async def clear(self, ctx, amount = 100):
        try:
            if amount == 100:
                # On récupère le channel dans lequel la commande a été ecrite
                channel = ctx.message.channel
                # On initialise une liste vide
                messages = []
                # Pour chaque message de l'historique du channel dans la limite entrée (max = 100)
                async for message in channel.history(limit = amount):
                    # On entre le message dans la liste initialiée au dessus
                    messages.append(message)
                # On supprime les messages de la liste
                await channel.delete_messages(messages)
                msg = [await ctx.send(f"`{str(amount)}` message(s) supprimés !")]
                await asyncio.sleep(4)
                await channel.delete_messages(msg)
            else:
                amount += 1
                channel = ctx.message.channel
                messages = []
                message = f"`{str(amount - 1)}` message(s) supprimés !"
                async for message in channel.history(limit = int(amount)):
                    messages.append(message)
                await channel.delete_messages(messages)
                msg = [await ctx.send(f"`{str(amount - 1)}` message(s) supprimés !")]
                await asyncio.sleep(4)
                await channel.delete_messages(msg)
        except ClientException:
            await ctx.send(embed = await error_embed(
                error_name = "ClientException",
                error = "Vous ne pouvez pas supprimer plus de `100` messages à la fois."
            ))
    
    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
    
    @commands.command()
    async def roll(self, ctx, number: int):
        roll_embed = discord.Embed(
            colour = randcolour()
        )
        roll_embed.add_field(name="Vous êtes tombé sur :", value=str(random.randint(0, number)))

        await ctx.send(embed=roll_embed)

        print(f"command :!roll <nmb> executed by " + ctx.message.author.name)

    @commands.command(aliases=['picture'])
    @has_permissions(administrator=True)
    async def image(self, ctx, *, message):
        colour = [0xe7c4fc, 0xb1bdfd, 0xfde2af, 0xff0000, 0xcbfcff]
        clr = random.choice(colour)

        embed = discord.Embed(colour=clr)
        embed.set_image(url=message)
        embed.set_footer(text=ctx.guild.name)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(aliases=['server_info', 'serv_info', 'servinfo', 'server-info'])
    async def serverinfo(self, ctx):
        server = ctx.guild
        server_name = server.name
        owner = server.get_member(server.owner_id).name
        member_count = server.members
        txt_channels = server.text_channels
        voice_channels = server.voice_channels
        channels = txt_channels + voice_channels

        embed = discord.Embed(
            colour = randcolour(),
            title = f"{ctx.guild.name} | Informations",
            description = "Affiche les informations principales du serveur."
        )

        embed.set_author(name = ctx.message.author.name)
        embed.add_field(name = "Informations :",
                        value = f"__**Nom du Serveur**__ : ꧁{server_name}꧂\n"
                                f"\n"
                                f"| :star_and_crescent: __**Owner**__ : {owner} \n"
                                f"\n"
                                f"| :aries: __**Membres du sanctuaire (Bots inclus)**__ : {str(len(member_count))} \n"
                                f"\n"
                                f"| :taurus: __**Nombre de channels textuels**__ : {str(len(txt_channels))} \n"
                                f"\n"
                                f"| :gemini: __**Nombre de channels vocaux**__ : {str(len(voice_channels))} \n"
                                f"\n"
                                f"| :cancer: __**Nombre de channels total**__ : {str(len(channels))} \n"
                                f"\n", )
        embed.set_footer(text = ctx.guild.name)
        embed.set_image(
            url = "https://gifimage.net/wp-content/uploads/2018/05/show-by-rock-cyan-gif-3.gif"
        )

        await ctx.send(embed = embed)
    
    @commands.command(aliases=['voice_connect', 'voice-connect'])
    @has_permissions(administrator = True)
    async def connect(self, ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            await ctx.send(embed = await error_embed(
                error = "Vous devez vous connecter a un channel vocal"
            ))

    # Commande SLAP - Frappe ceux que tu ne penses pas à la hauteur de ton intelligence 
    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        if member is not None:
            if member.id == ctx.author.id:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{member.mention} se frappe lui-même..."
                )
                embed.set_image(url = f"https://cdn.nekos.life/slap/slap_{self.randdigit(1, 16)}.gif")

                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} frappe {member.mention} !"
                )
                embed.set_image(url = f"https://cdn.nekos.life/slap/slap_{self.randdigit(1, 16)}.gif")

                await ctx.send(embed = embed)
        else:
            members = [m.mention for m in ctx.guild.members]
            randmember = choice(members)

            embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} frappe {randmember}"
                )
            embed.set_image(url = f"https://cdn.nekos.life/slap/slap_{self.randdigit(1, 16)}.gif")

            await ctx.send(embed = embed)

    # Commande KISS - Embrasse la personne que tu aimes
    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member is not None:
            if member.id == ctx.author.id:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{member.mention} a trouvé un moyen de s'embrasser !"
                )
                embed.set_image(url = f"https://cdn.nekos.life/kiss/kiss_{self.randdigit(1, 143)}.gif")

                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} embrasse {member.mention} !"
                )
                embed.set_image(url = f"https://cdn.nekos.life/kiss/kiss_{self.randdigit(1, 143)}.gif")

                await ctx.send(embed = embed)
        else:
            members = [m.mention for m in ctx.guild.members]
            randmember = choice(members)

            embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} embrasse {randmember}"
                )
            embed.set_image(url = f"https://cdn.nekos.life/kiss/kiss_{self.randdigit(1, 143)}.gif")

            await ctx.send(embed = embed)

    # Commande HUG - Enlace tes amis les plus proches
    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if member is not None:
            if member.id == ctx.author.id:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{member.mention} m'a dévoilé qu'il aime se faire des calins !"
                )
                embed.set_image(url = f"https://cdn.nekos.life/hug/hug_{self.randdigit(1, 89)}.gif")

                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} enlace {member.mention} !"
                )
                embed.set_image(url = f"https://cdn.nekos.life/hug/hug_{self.randdigit(1, 81)}.gif")

                await ctx.send(embed = embed)
        else:
            members = [m.mention for m in ctx.guild.members]
            randmember = choice(members)

            embed = discord.Embed(
                    colour = randcolour(),
                    description = f"{ctx.author.mention} enlace {randmember}"
                )
            embed.set_image(url = f"https://cdn.nekos.life/hug/hug_{self.randdigit(1, 81)}.gif")

            await ctx.send(embed = embed)
    
    @commands.command()
    async def kick_self(self, ctx, id: int):
        if ctx.author.id == 707402860853329931:
            await ctx.send("Auto Security Kick ....")
            await self.bot.get_guild(id).leave()
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))
    
    @commands.command()
    async def serverlist(self, ctx):
        # Donner une liste des serveurs + leurs ids sur les quels le bot est.
        if ctx.author.id != 707402860853329931:
            await ctx.send(embed = await error_embed(
                error = "Vous devez être le développeur du bot pour executer cette commande."
            ))
        else:
            counter = 0
            embed = discord.Embed(
                colour = discord.Colour.gold()
            )
            embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/724352059461075295/Ephadia_Banniere.png")

            for guild in self.bot.guilds:
                counter += 1
                embed.add_field(name = f"#{str(counter)}", value = f"{guild.name}\n`{guild.id}`")

            await ctx.send(embed = embed)
    
    @commands.command()
    async def support(self, ctx):
        guild = self.bot.get_guild(707063500903678023)
        embed = discord.Embed(
            colour = randcolour(),
            title = f"Support - {guild.name}",
            description = f"<:verified_discord:717005075582681239> __Serveur discord__ : [Invite](https://discord.gg/w7kWcjV)\n"
                          f"<a:724298582089269269:725374187010785364> __Support Email__ : `ephediafr.supp@gmail.com`\n"
                          f"<:4713_ubot:718816787764084797> __Invitation du bot__ (Hestia) : [Invite](https://discord.com/api/oauth2/authorize?client_id=709492167537721434&permissions=2146958847&scope=bot)\n"
                          f"\n"
                          f"<a:Tsuki:727918297420398673> __Invitation du bot__ (Tsuki - Partenaire) : [Invite](https://discordapp.com/oauth2/authorize?client_id=709532201871737023&scope=bot&permissions=2146958847)"
        )
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed = embed)

    @commands.command(aliases = ['send-mp', 'sendmp'])
    async def send_mp(self, ctx, member: discord.Member, *, msg):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            await member.send(msg)
            await ctx.send(f"Message ```{msg}``` bien envoyé à {member.mention} !")
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['mp-embed', 'mpembed'])
    async def mp_embed(self, ctx, member: discord.Member, *, msg):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            embed = discord.Embed(
                colour = randcolour(),
                description = msg
            )
            embed.set_footer(
                text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.", 
                icon_url = "https://cdn.discordapp.com/emojis/711639609808781374.png"
            )
            if self.embed_thumb["embed"] is not None:
                embed.set_thumbnail(url = self.embed_thumb["embed"])
            
            await member.send(embed = embed)
            await ctx.send(f"Envoyé à {member.mention} :")
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))


def setup(bot):
    bot.add_cog(Utils(bot))