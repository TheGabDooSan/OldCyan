import discord
from discord.ext import commands
from discord.utils import get
from main import randcolour, error_embed

import asyncio
import json
from math import *

class Inventories(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['create-banner'])
    async def create_banner(self, ctx, name, _type, rarity, url):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                banners = json.load(f)
            try:
                banners['banners'][name] = {}
                banners['banners'][name]['url'] = url
                banners['banners'][name]['type'] = _type
                banners['banners'][name]['rarity'] = rarity

                with open("cogs/items.json", "w") as f:
                    json.dump(banners, f, indent = 4)
            except json.JSONDecodeError:
                await ctx.send(embed = await error_embed(
                    error_name = "JSONDecodeError",
                    error = "Vous n'avez pas utilisé la commande de la bonne façon, `:!create-banner <name> <type> <rarity> <url>`"
                ))
            await ctx.message.delete()
            embed = discord.Embed(
                description = f"**Bannière créée avec succès !**\n> __Nom__ : {name}\n> __Type__ : {_type}\n> __Rareté__ : {rarity}\n> __Url__ : [LIEN]({url})",
                colour = randcolour()
            )
            embed.set_image(url = url)
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))
    
    @commands.command(aliases = ['create-title', 'create-titre'])
    async def create_title(self, ctx, name, *, value):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                titles = json.load(f)
            try:
                titles['titles'][name] = {}
                titles['titles'][name]['value'] = value

                with open("cogs/items.json", "w") as f:
                    json.dump(titles, f, indent = 4)
            except json.JSONDecodeError:
                await ctx.send(embed = await error_embed(
                    error_name = "JSONDecodeError",
                    error = "Vous n'avez pas utilisé la commande de la bonne façon, `:!create-title <name> <value>`"
                ))
            await ctx.message.delete()
            embed = discord.Embed(
                description = f"**Titre créé avec succès !**\n> __Nom__ : {name}\n> __Valeur__ : {value}",
                colour = randcolour()
            )
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['delete-banner', 'deletebanner', 'remove_banner', 'remove-banner', 'removebanner'])
    async def delete_banner(self, ctx, name):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                banners = json.load(f)
            with open("cogs/profile.json", "r") as f:
                profiles = json.load(f)
            if name in banners['banners']:
                banners['banners'].pop(name)
                await ctx.send(f"Vous avez bien supprimé la bannière : `{name}`")
                with open("cogs/profile.json", "w") as f:
                    json.dump(profiles, f, indent = 4)
                with open("cogs/items.json", "w") as f:
                    json.dump(banners, f, indent = 4)
            else:
                await ctx.send(embed = await error_embed(
                    error = "Cette bannière n'existe pas."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['delete-title', 'remove-title'])
    async def delete_title(self, ctx, name):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                titles = json.load(f)
            if name in titles['titles']:
                titles['titles'].pop(name)
                await ctx.send(f"Vous avez bien supprimé le titre : `{name}`")
                with open("cogs/items.json", "w") as f:
                    json.dump(titles, f, indent = 4)
            else:
                await ctx.send(embed = await error_embed(
                    error = "Ce titre n'existe pas."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))
    
    @commands.command(aliases = ['banners-list'])
    async def banners_list(self, ctx):
        with open("cogs/items.json", "r") as f:
            banners = json.load(f)
        max_page = 15

        first_run = True
        time_table = False
        num = 1
        counter = 0
        while True:
            if first_run:
                embed = discord.Embed(
                    title = f"Bannières [{len(banners['banners'])}]",
                    colour = randcolour(),
                    description = "Voici les bannières disponibles sur ce serveur :"
                )
                for banner in list(banners['banners'])[:25]:
                    embed.add_field(
                        name = banner,
                        value = f"{banners['banners'][banner]['type']} - {banners['banners'][banner]['rarity']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                first_run = False
                msg = await ctx.send(embed = embed)

            reactmoji = []
            if max_page == 1 and num == 1:
                pass
            elif num == 1:
                reactmoji.append('⏩')
            elif num == max_page:
                reactmoji.append('⏪')
            elif num > 1 and num < max_page:
                reactmoji.extend(['⏪', '⏩'])
            reactmoji.append('❌')

            for react in reactmoji:
                await msg.add_reaction(react)

            def check_react(reaction, user):
                if reaction.message.id != msg.id:
                    return False
                if user != ctx.message.author:
                    return False
                if str(reaction.emoji) not in reactmoji:
                    return False
                return True

            try:
                res, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check_react)
            except asyncio.TimeoutError:
                return await msg.clear_reactions()
            if user != ctx.message.author:
                pass
            elif '⏪' in str(res.emoji):
                counter -= 25
                num -= 1

                embed = discord.Embed(
                    title = f"Bannières [{len(banners['banners'])}]",
                    colour = randcolour(),
                    description = "Voici les bannières disponibles sur ce serveur :"
                )
                for banner in list(banners['banners'])[counter:]:
                    embed.add_field(
                        name = banner,
                        value = f"{banners['banners'][banner]['type']} - {banners['banners'][banner]['rarity']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏩' in str(res.emoji):
                counter += 25
                num += 1
                
                embed = discord.Embed(
                    title = f"Bannières [{len(banners['banners'])}]",
                    colour = randcolour(),
                    description = "Voici les bannières disponibles sur ce serveur :"
                )
                for banner in list(banners['banners'])[counter:]:
                    embed.add_field(
                        name = banner,
                        value = f"{banners['banners'][banner]['type']} - {banners['banners'][banner]['rarity']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '❌' in str(res.emoji):
                embed = discord.Embed(
                    description = "Vous avez fermé la page : `:!banners-list`",
                    colour = randcolour()
                )
                reactmoji = []
                await msg.clear_reactions()
                await msg.edit(embed = embed)

    @commands.command(aliases = ['titles-list', 'titleslist'])
    async def titles_list(self, ctx):
        with open("cogs/items.json", "r") as f:
            titles = json.load(f)
        max_page = 15

        first_run = True
        time_table = False
        num = 1
        counter = 0
        while True:
            if first_run:
                embed = discord.Embed(
                    title = f"Titres [{len(titles['titles'])}]",
                    colour = randcolour(),
                    description = "Voici les titres disponibles sur ce serveur :"
                )
                for title in list(titles['titles'])[:25]:
                    embed.add_field(
                        name = title,
                        value = f"{title} - {titles['titles'][title]['value']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                first_run = False
                msg = await ctx.send(embed = embed)

            reactmoji = []
            if max_page == 1 and num == 1:
                pass
            elif num == 1:
                reactmoji.append('⏩')
            elif num == max_page:
                reactmoji.append('⏪')
            elif num > 1 and num < max_page:
                reactmoji.extend(['⏪', '⏩'])
            reactmoji.append('❌')

            for react in reactmoji:
                await msg.add_reaction(react)

            def check_react(reaction, user):
                if reaction.message.id != msg.id:
                    return False
                if user != ctx.message.author:
                    return False
                if str(reaction.emoji) not in reactmoji:
                    return False
                return True

            try:
                res, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check_react)
            except asyncio.TimeoutError:
                return await msg.clear_reactions()
            if user != ctx.message.author:
                pass
            elif '⏪' in str(res.emoji):
                counter -= 25
                num -= 1

                embed = discord.Embed(
                    title = f"Titres [{len(titles['titles'])}]",
                    colour = randcolour(),
                    description = "Voici les titres disponibles sur ce serveur :"
                )
                for title in list(titles['titles'])[counter:]:
                    embed.add_field(
                        name = title,
                        value = f"{title} - {titles['titles'][title]['value']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏩' in str(res.emoji):
                counter += 25
                num += 1
                
                embed = discord.Embed(
                    title = f"Titres [{len(titles['titles'])}]",
                    colour = randcolour(),
                    description = "Voici les titres disponibles sur ce serveur :"
                )
                for title in list(titles['titles'])[counter:]:
                    embed.add_field(
                        name = title,
                        value = f"{title} - {titles['titles'][title]['value']}"
                    )

                embed.set_image(url = "https://cdn.discordapp.com/attachments/726913124321722490/726944493969997885/encyclopedie.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/15")

                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '❌' in str(res.emoji):
                embed = discord.Embed(
                    description = "Vous avez fermé la page : `:!titles-list`",
                    colour = randcolour()
                )
                reactmoji = []
                await msg.clear_reactions()
                await msg.edit(embed = embed)
    
    @commands.command(aliases = ['banner-info'])
    async def banner_info(self, ctx, name):
        with open("cogs/items.json", "r") as f:
            banners = json.load(f)
        if name in banners['banners']:
            current_banner = banners['banners'][name]
            embed = discord.Embed(
                colour = randcolour(),
                title = name,
                description = f"__Nom__ : `{name}`\n__Type__ : `{current_banner['type']}`\n__Rareté__ : {current_banner['rarity']}\n__Url__ :"
            )
            embed.set_image(url = current_banner['url'])
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error = f"La bannière `{name}` n'existe pas."
            ))
    
    @commands.command()
    async def give(self, ctx, param, member: discord.Member, item_name):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/profile.json", "r") as f:
                    profiles = json.load(f)
            if str(member.id) in profiles:
                if param == "banner" or param == "banniere":
                    with open("cogs/items.json", "r") as f:
                        banners = json.load(f)
                    if item_name in banners['banners']:
                        inventory = profiles[str(member.id)]['inv']['banners']
                        if item_name not in inventory:
                            inventory.append(item_name)
                            with open("cogs/profile.json", "w") as f:
                                json.dump(profiles, f, indent = 4)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"{member.mention} a gagné la bannière  {item_name} !"
                            )
                            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                            await ctx.send(f"La bannière {item_name} a bien été ajoutée a l'inventaire de {member.name} !")
                        else:
                            await ctx.send(embed = await error_embed(
                                error = f"Le membre {member.mention} a déjà cette bannière."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = f"La bannière `{item_name}` n'existe pas."
                        ))
                elif param == "titre" or param == "title":
                    with open("cogs/items.json", "r") as f:
                        titles = json.load(f)
                    if item_name in titles['titles']:
                        inventory = profiles[str(member.id)]['inv']['titles']
                        if item_name not in inventory:
                            inventory.append(item_name)
                            with open("cogs/profile.json", "w") as f:
                                json.dump(profiles, f, indent = 4)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"{member.mention} a gagné le titre {item_name} !"
                            )
                            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                            await ctx.send(f"Le titre {item_name} a bien été ajouté a l'inventaire de {member.name} !")
                        else:
                            await ctx.send(embed = await error_embed(
                                error = f"Le membre {member.mention} a déjà ce titre."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = f"Le titre `{item_name}` n'existe pas."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Entrez un paramètre valide. (`banner`/`title`)."
                    ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['inventory'])
    async def inv(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        inv = profiles[str(member.id)]['inv']
        if str(member.id) in profiles:
            if len(inv['banners'] + inv['titles']) < 30:
                member_banners = "\n".join(f"• [{items['banners'][x]['type']}] {x} - {items['banners'][x]['rarity']}" for x in profiles[str(member.id)]['inv']['banners'])
                member_titles = "\n".join(f"• {x} - {items['titles'][x]['value']}" for x in profiles[str(member.id)]['inv']['titles'])
                embed = discord.Embed(
                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                    description = f"Inventaire de {member} :",
                    colour = randcolour()
                )
                embed.add_field(name = "<a:flecheimageanimee0010:727574818110832691> **Bannières**", value = member_banners or "Aucune bannière", inline = False)
                embed.add_field(name = "<a:flecheimageanimee0010:727574818110832691> **Titres**", value = member_titles or "Aucun titre", inline = False)
                embed.set_thumbnail(url = member.avatar_url)
                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    colour = randcolour(),
                    description = "Votre inventaire dépasse les 30 objets, voulez-vous recevoir votre inventaire de **``banners``** ou de **``titles``** ?"
                )
                embed.set_footer(text = "Expiration : 30s")
                await ctx.send(embed = embed)

                def check(m):
                    return m.channel == ctx.channel and m.target == member
                
                try:
                    msg = await self.bot.wait_for('message', timeout = 30, check = lambda message: message.author == member and message.channel == ctx.channel)
                    if msg.content.lower() == "banners" or msg.content.lower() == "bannieres":
                        '''
                        ENVOI DE L'INVENTAIRE DE BANNIERES
                        '''
                        MAX_PAGES_BANNERS = ceil(len(inv['banners']) / 15)
                        MAX_PAGES_TITLES = ceil(len(inv['titles']) / 15)

                        first_run = True
                        num = 1
                        counter = 0 
                        while True:
                            if first_run:
                                member_banners = "\n".join(f"• [{items['banners'][x]['type']}] {x} - {items['banners'][x]['rarity']}" for x in list(profiles[str(member.id)]['inv']['banners'])[:15])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Bannières [{len(inv['banners'])}]**", value = member_banners or "Aucune bannière", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_BANNERS}")

                                first_run = False
                                msg = await ctx.send(embed = embed)

                            reactmoji = []
                            if MAX_PAGES_BANNERS == 1 and num == 1:
                                pass
                            elif num == 1:
                                reactmoji.append('▶️')
                            elif num == MAX_PAGES_BANNERS:
                                reactmoji.append('◀️')
                            elif num > 1 and num < MAX_PAGES_BANNERS:
                                reactmoji.extend(['◀️', '▶️'])
                            reactmoji.append('❌')

                            for react in reactmoji:
                                await msg.add_reaction(react)

                            def check_react(reaction, user):
                                if reaction.message.id != msg.id:
                                    return False
                                if user != ctx.message.author:
                                    return False
                                if str(reaction.emoji) not in reactmoji:
                                    return False
                                return True

                            try:
                                res, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check_react)
                            except asyncio.TimeoutError:
                                return await msg.clear_reactions()
                            if user != ctx.message.author:
                                pass
                            elif '◀️' in str(res.emoji):
                                counter -= 15
                                num -= 1
                                rest = len(inv['banners']) - (counter + 15)
                                
                                member_banners = "\n".join(f"• [{items['banners'][x]['type']}] {x} - {items['banners'][x]['rarity']}" for x in list(profiles[str(member.id)]['inv']['banners'])[counter:-rest])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Bannières [{len(inv['banners'])}]**", value = member_banners or "Aucune bannière", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_BANNERS}")

                                await msg.clear_reactions()
                                await msg.edit(embed=embed)
                            elif '▶️' in str(res.emoji):
                                counter += 15
                                num += 1
                                if num == MAX_PAGES_BANNERS:
                                    rest = 1
                                else:
                                    rest = len(inv['banners']) - (counter + 15)

                                member_banners = "\n".join(f"• [{items['banners'][x]['type']}] {x} - {items['banners'][x]['rarity']}" for x in list(profiles[str(member.id)]['inv']['banners'])[counter:-rest])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Bannières [{len(inv['banners'])}]**", value = member_banners or "Aucune bannière", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_BANNERS}")

                                await msg.clear_reactions()
                                await msg.edit(embed=embed)
                            elif '❌' in str(res.emoji):
                                embed = discord.Embed(
                                    description = "Vous avez fermé la page : `:!inv`",
                                    colour = randcolour()
                                )
                                reactmoji = []
                                await msg.clear_reactions()
                                await msg.edit(embed = embed)
                    elif msg.content.lower() == "titles" or msg.content.lower() == "titres":
                        '''
                        ENVOI DE L'INVENTAIRE DE TITRES
                        '''
                        MAX_PAGES_BANNERS = ceil(len(inv['banners']) / 15)
                        MAX_PAGES_TITLES = ceil(len(inv['titles']) / 15)

                        first_run = True
                        num = 1
                        counter = 0 
                        while True:
                            if first_run:
                                member_titles = "\n".join(f"• {x} - {items['titles'][x]['value']}" for x in list(profiles[str(member.id)]['inv']['titles'])[:15])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Titres [{len(inv['titles'])}]**", value = member_titles or "Aucun titre", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_TITLES}")

                                first_run = False
                                msg = await ctx.send(embed = embed)

                            reactmoji = []
                            if MAX_PAGES_TITLES == 1 and num == 1:
                                pass
                            elif num == 1:
                                reactmoji.append('▶️')
                            elif num == MAX_PAGES_TITLES:
                                reactmoji.append('◀️')
                            elif num > 1 and num < MAX_PAGES_TITLES:
                                reactmoji.extend(['◀️', '▶️'])
                            reactmoji.append('❌')

                            for react in reactmoji:
                                await msg.add_reaction(react)

                            def check_react(reaction, user):
                                if reaction.message.id != msg.id:
                                    return False
                                if user != ctx.message.author:
                                    return False
                                if str(reaction.emoji) not in reactmoji:
                                    return False
                                return True

                            try:
                                res, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check_react)
                            except asyncio.TimeoutError:
                                return await msg.clear_reactions()
                            if user != ctx.message.author:
                                pass
                            elif '◀️' in str(res.emoji):
                                counter -= 15
                                num -= 1
                                rest = len(inv['titles']) - (counter + 15)
                                
                                member_titles = "\n".join(f"• {x} -  {items['titles'][x]['value']}" for x in list(profiles[str(member.id)]['inv']['titles'])[counter:-rest])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Titres [{len(inv['titles'])}]**", value = member_titles or "Aucun titre", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_TITLES}")

                                await msg.clear_reactions()
                                await msg.edit(embed=embed)
                            elif '▶️' in str(res.emoji):
                                counter += 15
                                num += 1
                                if num == MAX_PAGES_TITLES:
                                    rest = 1
                                else:
                                    rest = len(inv['titles']) - (counter + 15)

                                member_titles = "\n".join(f"• {x} -  {items['titles'][x]['value']}" for x in list(profiles[str(member.id)]['inv']['titles'])[counter:-rest])
                                embed = discord.Embed(
                                    title = f"**__❦ ► Inventaire ◄ ❦__**",
                                    description = f"Inventaire de {member} :",
                                    colour = randcolour()
                                )
                                embed.add_field(name = f"<a:flecheimageanimee0010:727574818110832691> **Titres [{len(inv['titles'])}]**", value = member_titles or "Aucun titre", inline = False)
                                embed.set_thumbnail(url = member.avatar_url)
                                embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/727525486640627723/InventaireImage.png")
                                embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{MAX_PAGES_TITLES}")

                                await msg.clear_reactions()
                                await msg.edit(embed=embed)
                            elif '❌' in str(res.emoji):
                                embed = discord.Embed(
                                    description = "Vous avez fermé la page : `:!inv`",
                                    colour = randcolour()
                                )
                                reactmoji = []
                                await msg.clear_reactions()
                                await msg.edit(embed = embed)
                except asyncio.TimeoutError:
                    await ctx.send("Votre demande d'inventaire a expirée.")                        
        else:
            await ctx.send(embed = await error_embed(
                error = f"{member.mention} n'est pas enregistré (`:!register`)"
            ))
    
    @commands.command()
    async def use(self, ctx, param, name):
        if param == "banner" or param == "banniere":
            with open("cogs/profile.json", "r") as f:
                profiles = json.load(f)
            with open("cogs/items.json", "r") as f:
                items = json.load(f)
            if name in items['banners']:
                if name in profiles[str(ctx.author.id)]['inv']['banners']:
                    profiles[str(ctx.author.id)]['image'] = items['banners'][name]['url']
                    embed = discord.Embed(
                        colour = randcolour(),
                        description = f"Vous venez d'equiper la bannière `{name} - {items['banners'][name]['rarity']}`"
                    )
                    embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                    await ctx.send(embed = embed)
                    with open("cogs/profile.json", "w") as f:
                        json.dump(profiles, f, indent = 4)
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Vous ne possedez pas cette bannière."
                    ))
            else:
                await ctx.send(embed = await error_embed(
                    error = "Cette bannière n'existe pas, veillez a bien écrire le nom de la bannière avec les majuscules."
                ))
        elif param == "title" or param == "titre":
            with open("cogs/profile.json", "r") as f:
                profiles = json.load(f)
            with open("cogs/items.json", "r") as f:
                items = json.load(f)
            if name in items['titles']:
                if name in profiles[str(ctx.author.id)]['inv']['titles']:
                    profiles[str(ctx.author.id)]['titre'] = items['titles'][name]['value']
                    embed = discord.Embed(
                        colour = randcolour(),
                        description = f"Vous venez d'equiper le titre `{name}` - `{items['titles'][name]['value']}`"
                    )
                    embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                    await ctx.send(embed = embed)
                    with open("cogs/profile.json", "w") as f:
                        json.dump(profiles, f, indent = 4)
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Vous ne possedez pas ce titre."
                    ))
            else:
                await ctx.send(embed = await error_embed(
                    error = "Ce titre n'existe pas, veillez a bien écrire le nom du titre avec les majuscules."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous n'avez pas choisi le bon paramètre. (`banner`/`title`)"
            ))

    @commands.command(aliases = ['take-item', 'takeitem', 'take'])
    async def take_item(self, ctx, param, member: discord.Member, item_name):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/profile.json", "r") as f:
                    profiles = json.load(f)
            if str(member.id) in profiles:
                if param == "banner" or param == "banniere":
                    with open("cogs/items.json", "r") as f:
                        banners = json.load(f)
                    if item_name in banners['banners']:
                        inventory = profiles[str(member.id)]['inv']['banners']
                        if item_name in inventory:
                            inventory.remove(item_name)
                            with open("cogs/profile.json", "w") as f:
                                json.dump(profiles, f, indent = 4)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"La bannière {item_name} a bien été supprimée de l'inventaire de {member.mention}."
                            )
                            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                            await ctx.send(embed = embed)
                        else:
                            await ctx.send(embed = await error_embed(
                                error = f"Le membre {member.mention} n'a pas cette bannière."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = f"La bannière `{item_name}` n'existe pas."
                        ))
                elif param == "titre" or param == "title":
                    with open("cogs/items.json", "r") as f:
                        titles = json.load(f)
                    if item_name in titles['titles']:
                        inventory = profiles[str(member.id)]['inv']['titles']
                        if item_name in inventory:
                            inventory.remove(item_name)
                            with open("cogs/profile.json", "w") as f:
                                json.dump(profiles, f, indent = 4)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"Le titre {item_name} a bien été supprimé de l'inventaire de {member.mention}."
                            )
                            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                            await ctx.send(embed = embed)
                        else:
                            await ctx.send(embed = await error_embed(
                                error = f"Le membre {member.mention} n'a pas ce titre."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = f"Le titre `{item_name}` n'existe pas."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Entrez un paramètre valide. (`banner`/`title`)."
                    ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))


def setup(bot):
    bot.add_cog(Inventories(bot))