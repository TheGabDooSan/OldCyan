import discord
from discord.ext import commands
from discord.utils import get
from main import randcolour, error_embed

from math import ceil

import asyncio, random, json

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['balance', 'magiccoins', 'magic-coins', 'magic_coins', 'bal'])
    async def money(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)
        if str(member.id) in profiles:
            embed = discord.Embed(
                colour = randcolour(),
            )
            embed.set_author(name = member, icon_url = member.avatar_url)
            embed.add_field(
                name = "MagicCoins :",
                value = f"<a:MagicCoins:728621926809075732> {profiles[str(member.id)]['balance']}"
            )
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error = f"{member.mention} n'est pas enregistré. (`:!register`)"
            ))
    
    @commands.command(aliases = ['hourly-gain', 'random-gain'])
    async def hourlygain(self, ctx, _min, _max, cmd = None):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                items = json.load(f)
            if cmd.lower() == "work" or cmd.lower() == "crime" or cmd.lower() == "battle":
                min_value = items['hourly'][cmd]['min'] = int(_min)
                max_value = items['hourly'][cmd]['max'] = int(_max)
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"Vous venez de changer le taux d'argent gagné par la commande {cmd} a **{min_value}** - **{max_value}** (__Moyenne__: **{(min_value + max_value) / 2}**)"
                )
                embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                with open("cogs/items.json", "w") as f:
                    json.dump(items, f, indent = 4)
                await ctx.send(embed = embed)
            elif cmd == None:
                min_value = items['hourly']['work']['min'] = int(_min)
                max_value = items['hourly']['work']['max'] = int(_max)
                items['hourly']['battle']['min'] = int(_min)
                items['hourly']['battle']['max'] = int(_max)
                items['hourly']['crime']['min'] = int(_min)
                items['hourly']['crime']['max'] = int(_max)
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"Vous venez de changer le taux d'argent gagné par les commandes `work`, `battle` et `crime` a **{min_value}** - **{max_value}** (__Moyenne__: **{(min_value + max_value) / 2}**)"
                )
                embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                with open("cogs/items.json", "w") as f:
                    json.dump(items, f, indent = 4)
                await ctx.send(embed = embed)
            else:
                await ctx.send(embed = await error_embed(
                    error = f"La commande `{cmd}` n'existe pas."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def work(self, ctx):
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)

        if str(ctx.author.id) in profiles:
            _min = items['hourly']['work']['min']
            _max = items['hourly']['work']['max']

            random_gain = random.randint(_min, _max)
            profiles[str(ctx.author.id)]['balance'] += random_gain

            with open("cogs/profile.json", "w") as f:
                json.dump(profiles, f, indent = 4)

            randmsg = random.choice(list(items['hourly']['work']['messages'].values()))

            embed = discord.Embed(
                colour = randcolour(),
                description = randmsg.replace("{gain}", f"<a:MagicCoins:728621926809075732>{random_gain}")
            )
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
            print("Work")
        else:
            await ctx.send(embed = await error_embed(
                error = f"Vous n'êtes pas enregistré. (`:!register`)"
            ))

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def battle(self, ctx):
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)

        if str(ctx.author.id) in profiles:
            _min = items['hourly']['battle']['min']
            _max = items['hourly']['battle']['max']

            random_gain = random.randint(_min, _max)
            profiles[str(ctx.author.id)]['balance'] += random_gain

            with open("cogs/profile.json", "w") as f:
                json.dump(profiles, f, indent = 4)

            randmsg = random.choice(list(items['hourly']['battle']['messages'].values()))

            embed = discord.Embed(
                colour = randcolour(),
                description = randmsg.replace("{gain}", f"<a:MagicCoins:728621926809075732>{random_gain}")
            )
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
            print("Battle")
        else:
            await ctx.send(embed = await error_embed(
                error = f"Vous n'êtes pas enregistré. (`:!register`)"
            ))

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def crime(self, ctx):
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)

        if str(ctx.author.id) in profiles:
            _min = items['hourly']['crime']['min']
            _max = items['hourly']['crime']['max']

            random_gain = random.randint(_min, _max)
            profiles[str(ctx.author.id)]['balance'] += random_gain

            with open("cogs/profile.json", "w") as f:
                json.dump(profiles, f, indent = 4)

            randmsg = random.choice(list(items['hourly']['crime']['messages'].values()))

            embed = discord.Embed(
                colour = randcolour(),
                description = randmsg.replace("{gain}", f"<a:MagicCoins:728621926809075732>{random_gain}")
            )
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
            print("Crime")
        else:
            await ctx.send(embed = await error_embed(
                error = f"Vous n'êtes pas enregistré. (`:!register`)"
            ))

    @commands.command(aliases = ['hourly-message', 'hourly-msg', 'hourlymsg'])
    async def hourlymessage(self, ctx, cmd, *, message = None):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                items = json.load(f)
            if cmd == "work" or cmd == "battle" or cmd == "crime":
                if message is not None:
                    index = str(len(list(items['hourly'][cmd]['messages'].keys())) + 1)
                    items['hourly'][cmd]['messages'][index] = message
                    embed = discord.Embed(
                        colour = randcolour(),
                        description = f"Le message ```{message}``` a bien été ajouté a la liste des messages de la commande {cmd} (__index__ = {index})"
                    )
                    await ctx.send(embed = embed)
                    with open("cogs/items.json", "w") as f:
                        json.dump(items, f, indent = 4)
                else:
                    embed = discord.Embed(
                        colour = randcolour(),
                        description = f"Voici la liste des messages disponibles pour la commande {cmd}"
                    )
                    counter = 0
                    for message in list(items['hourly'][cmd]['messages'].values()):
                        counter += 1
                        embed.add_field(
                            name = f"Index {counter}",
                            value = items['hourly'][cmd]['messages'][str(counter)]
                        )
                    embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                    await ctx.send(embed = embed)
            else:
                await ctx.send(embed = await error_embed(
                    error = f"La commande `{cmd}` n'existe pas."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['give-money', 'give_money'])
    async def givemoney(self, ctx, member: discord.Member, amount: int):
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)
        if str(ctx.author.id) in profiles:
            if str(member.id) in profiles:
                if ctx.author.id != member.id:
                    gained_money = f"<a:MagicCoins:728621926809075732>{amount}"
                    if (profiles[str(ctx.author.id)]['balance'] - amount) >= 0:
                        profiles[str(member.id)]['balance'] += amount
                        profiles[str(ctx.author.id)]['balance'] -= amount
                        with open("cogs/profile.json", "w") as f:
                            json.dump(profiles, f, indent = 4)
                        await ctx.send(f"Vous avez bien donné {gained_money} Magic Coins à {member.mention}")
                    else:
                        await ctx.send(embed = await error_embed(
                            error = f"Vous n'avez pas assez d'argent pour donner {gained_money} Magic Coins."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Vous ne pouvez pas vous donner de l'argent a vous même..."
                    ))
            else:
                await ctx.send(embed = await error_embed(
                    error = f"{member.mention} n'est pas enregistré(e). (`:!register`)"
                ))
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous devez être enregistré(e) pour executer cette commande. (`:!register`)"
            ))

    @commands.command(aliases = ['add-money', 'add_money'])
    async def addmoney(self, ctx, member: discord.Member, amount):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/profile.json", "r") as f:
                profiles = json.load(f)
            if str(member.id) in profiles.keys():
                profiles[str(member.id)]['balance'] += int(amount)
                with open("cogs/profile.json", "w") as f:
                    json.dump(profiles, f, indent = 4)
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"Vous avez donné <a:MagicCoins:728621926809075732>{amount} Magic Coins à {member.mention}."
                )
                embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                await ctx.send(embed = embed)
            else:
                await ctx.send(embed = await error_embed(
                    error = f"{member.mention} n'est pas enregistré(e). (`:!register`)"
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['take-money', 'take_money'])
    async def takemoney(self, ctx, member: discord.Member, amount):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/profile.json", "r") as f:
                profiles = json.load(f)
            if str(member.id) in profiles.keys():
                profiles[str(member.id)]['balance'] -= int(amount)
                with open("cogs/profile.json", "w") as f:
                    json.dump(profiles, f, indent = 4)
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"Vous avez enlevé <a:MagicCoins:728621926809075732>{amount} Magic Coins à {member.mention}."
                )
                embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
                await ctx.send(embed = embed)
            else:
                await ctx.send(embed = await error_embed(
                    error = f"{member.mention} n'est pas enregistré(e). (`:!register`)"
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))
    
    @commands.command(aliases = ['add-shop-item', 'add-shop'])
    async def addshopitem(self, ctx, param, name, price, *, desc):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            with open("cogs/items.json", "r") as f:
                items = json.load(f)
            param = param.lower()
            if param == "banner" or param == "banniere" or param == "bannière":
                if name in items['banners']:
                    items['shop']['banners'][name] = {}
                    items['shop']['banners'][name]['price'] = int(price)
                    items['shop']['banners'][name]['desc'] = desc
                    embed = discord.Embed(
                        description = f"Bannière __{name}__ ajoutée a la boutique avec succès !\nPlus d'informations sur la bannière : `:!banner-info {name}`\nDescription : ```{desc}```",
                        colour = randcolour()
                    )
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    await ctx.send(embed = await error_embed(
                        error = "La bannière que vous essayez d'ajouter a la boutique n'existe pas."
                    ))
            elif param == "title" or param == "titre":
                if name in items['titles']:
                    items['shop']['titles'][name] = {}
                    items['shop']['titles'][name]['price'] = int(price)
                    items['shop']['titles'][name]['desc'] = desc
                    embed = discord.Embed(
                        description = f"Titre __{name}__ ajoutée a la boutique avec succès !\nDescription : ```{desc}```",
                        colour = randcolour()
                    )
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Le titre que vous essayez d'ajouter a la boutique n'existe pas."
                    ))
            else:
                await ctx.send(embed = await error_embed(
                    error = f"Le paramètre ``{param}`` est invalide. (`banner`, `title`)"
                ))
            with open("cogs/items.json", "w") as f:
                json.dump(items, f, indent = 4)
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command()
    async def buy(self, ctx, param, name, nmb = None):
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        with open("cogs/guilds.json", "r") as f:
            guilds = json.load(f)
        if str(ctx.author.id) in profiles:
            if param == "banner" or param == "banniere":
                if name in items['shop']['banners']:
                    if name not in profiles[str(ctx.author.id)]['inv']['banners']:
                        if profiles[str(ctx.author.id)]['balance'] >= items['shop']['banners'][name]['price']:
                            profiles[str(ctx.author.id)]['balance'] -= items['shop']['banners'][name]['price']
                            profiles[str(ctx.author.id)]['inv']['banners'].append(name)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"Vous avez bien acheté la bannière `{name}` pour <a:MagicCoins:728621926809075732>{items['shop']['banners'][name]['price']} Magic Coins."
                            )
                            await ctx.send(embed = embed)
                        else:
                            await ctx.send(embed = await error_embed(
                                error = "Vous n'avez pas assez d'argent pour acheter cette bannière."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = "Vous possedez déjà cette bannière."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Cette bannière n'existe pas ou n'est pas vendu dans le shop."
                    ))
            elif param == "title" or param == "titre":
                if name in items['shop']['titles']:
                    if name not in profiles[str(ctx.author.id)]['inv']['titles']:
                        if profiles[str(ctx.author.id)]['balance'] >= items['shop']['titles'][name]['price']:
                            profiles[str(ctx.author.id)]['balance'] -= items['shop']['titles'][name]['price']
                            profiles[str(ctx.author.id)]['inv']['titles'].append(name)
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"Vous avez bien acheté le titre `{name}` pour <a:MagicCoins:728621926809075732>{items['shop']['titles'][name]['price']} Magic Coins."
                            )
                            await ctx.send(embed = embed)
                        else:
                            await ctx.send(embed = await error_embed(
                                error = "Vous n'avez pas assez d'argent pour acheter ce titre."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = "Vous possedez déjà ce titre."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Ce titre n'existe pas ou n'est pas vendu dans le shop."
                    ))
            elif param == "contrib" or param == "contribution":
                if nmb is None:
                    nmb = 1
                nmb = int(nmb)
                if name in items['shop']['divers']['contrib']:
                    if profiles[str(ctx.author.id)]['balance'] >= items['shop']['divers']['contrib'][name]:
                        if nmb > 0:
                            profiles[str(ctx.author.id)]['balance'] -= items['shop']['divers']['contrib'][name] * nmb
                            guilds['guilds'][name]['contrib'] += nmb
                            print(guilds['guilds'][name]['contrib'])
                            embed = discord.Embed(
                                colour = randcolour(),
                                description = f"Vous avez bien acheté {nmb} contribution(s) [`{name}`] pour <a:MagicCoins:728621926809075732>{items['shop']['divers']['contrib'][name] * nmb} ({items['shop']['divers']['contrib'][name]} x {nmb}) Magic Coins. Nombre actuel de contributions de cette guilde : {guilds['guilds'][name]['contrib']}"
                            )
                            await ctx.send(embed = embed)
                        else:
                            await ctx.send(embed = await error_embed(
                                error = "Vous devez acheter au moins une contribution."
                            ))
                    else:
                        await ctx.send(embed = await error_embed(
                            error = "Vous n'avez pas assez d'argent pour acheter cet objet."
                        ))
                else:
                    await ctx.send(embed = await error_embed(
                        error = "Cette guilde n'existe pas."
                    ))
            else:
                await ctx.send(embed = await error_embed(
                    error = f"Le paramètre `{param}` n'est pas valide. (`banner`, `title`, `contrib`)"
                ))
            with open("cogs/profile.json", "w") as f:
                json.dump(profiles, f, indent = 4)
            with open("cogs/items.json", "w") as f:
                json.dump(items, f, indent = 4)
            with open("cogs/guilds.json", "w") as f:
                json.dump(guilds, f, indent = 4)
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous devez d'abord vous enregistrer pour executer cette commande. (`:!register`)"
            ))

    @commands.command(aliases = ['delete-shop-item', 'remove-shop-item', 'remove-shop', 'delete-shop'])
    async def removeshopitem(self, ctx, param, name):
        pass

    @commands.command(aliases = ['boutique'])
    async def shop(self, ctx, param):
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        if param.lower() == 'banners' or param.lower() == "bannieres" or param.lower() == "bannières":
            max_page = ceil(len(items['shop']['banners']) / 15)

            first_run = True
            time_table = False
            num = 1
            counter = 0
            while True:
                if first_run:
                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des bannières en vente dans la boutique"
                    )
                    for x in list(items['shop']['banners'].keys())[:15]:
                        embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['banners'][x]['price']}\n{items['shop']['banners'][x]['desc']}" or "Aucune bannière")

                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

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
                    res, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check_react)
                except asyncio.TimeoutError:
                    return await msg.clear_reactions()
                if user != ctx.message.author:
                    pass
                elif '⏪' in str(res.emoji):
                    counter -= 15
                    num -= 1
                    rest = len(items['shop']['banners']) - (counter + 15)
                    
                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des bannières en vente dans la boutique"
                    )
                    if num == 1:
                    	for x in list(items['shop']['banners'].keys())[:15]:
                        	embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['banners'][x]['price']}\n{items['shop']['banners'][x]['desc']}" or "Aucune bannière")
                    else:
                    	for x in list(items['shop']['banners'].keys())[counter:-rest]:
                        	embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['banners'][x]['price']}\n{items['shop']['banners'][x]['desc']}" or "Aucune bannière")

                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

                    await msg.clear_reactions()
                    await msg.edit(embed=embed)
                elif '⏩' in str(res.emoji):
                    counter += 15
                    num += 1
                    rest = len(items['shop']['banners']) - (counter + 15)
                    if num == max_page:
                        rest = 1
                    
                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des bannières en vente dans la boutique"
                    )
                    for x in list(items['shop']['banners'].keys())[counter:-rest]:
                        embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['banners'][x]['price']}\n{items['shop']['banners'][x]['desc']}" or "Aucune bannière")

                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

                    await msg.clear_reactions()
                    await msg.edit(embed=embed)
                elif '❌' in str(res.emoji):
                    embed = discord.Embed(
                        description = "Vous avez fermé la page : `:!shop banners`",
                        colour = randcolour()
                    )
                    reactmoji = []
                    await msg.clear_reactions()
                    await msg.edit(embed = embed)
        elif param.lower() == 'titles' or param.lower() == "titres" or param.lower() == "titre":
            max_page = ceil(len(items['shop']['titles']))

            first_run = True
            time_table = False
            num = 1
            counter = 0
            maximum = len(list(items['shop']['titles']))
            while True:
                if first_run:
                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des titres en vente dans la boutique"
                    )
                    for x in list(items['shop']['titles'].keys())[:15]:
                        embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['titles'][x]['price']}\n{items['shop']['titles'][x]['desc']}" or "Aucun titre")
                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

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
                    res, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check_react)
                except asyncio.TimeoutError:
                    return await msg.clear_reactions()
                if user != ctx.message.author:
                    pass
                elif '⏪' in str(res.emoji):
                    counter -= 15
                    num -= 1
                    rest = len(items['shop']['titles']) - (counter + 15)

                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des titres en vente dans la boutique"
                    )
                    if num == 1:
                    	for x in list(items['shop']['titles'].keys())[:15]:
                        	embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['titles'][x]['price']}\n{items['shop']['titles'][x]['desc']}" or "Aucun titre")
                    else:
                    	for x in list(items['shop']['titles'].keys())[counter:-rest]:
                    		embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['titles'][x]['price']}\n{items['shop']['titles'][x]['desc']}" or "Aucun titre")
                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

                    await msg.clear_reactions()
                    await msg.edit(embed=embed)
                elif '⏩' in str(res.emoji):
                    counter += 25
                    num += 1
                    rest = len(items['shop']['titles']) - (counter + 15)
                    if num == max_page:
                        rest = 1
                    
                    embed = discord.Embed(
                        colour = randcolour(),
                        title = "Boutique",
                        description = "Voici la liste des titres en vente dans la boutique"
                    )
                    for x in list(items['shop']['titles'].keys())[counter:-rest]:
                        embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['titles'][x]['price']}\n{items['shop']['titles'][x]['desc']}" or "Aucun titre")
                    embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
                    embed.set_footer(text = f"Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS. | Page {num}/{max_page}")

                    await msg.clear_reactions()
                    await msg.edit(embed=embed)
                elif '❌' in str(res.emoji):
                    embed = discord.Embed(
                        description = "Vous avez fermé la page : `:!shop titles`",
                        colour = randcolour()
                    )
                    reactmoji = []
                    await msg.clear_reactions()
                    await msg.edit(embed = embed)
        elif param.lower() == 'others' or param.lower() == "autre" or param.lower() == "divers":
            embed = discord.Embed(
                colour = randcolour(),
                title = "Boutique",
                description = "Voici la liste des objets divers en vente dans la boutique"
            )
            for x in list(items['shop']['divers'].keys()):
                embed.add_field(name = "** **", value = f"• **{x}** - <a:MagicCoins:728621926809075732>{items['shop']['divers'][x]['price']}\n{items['shop']['divers'][x]['desc']}" or "Aucun objet", inline = False)
            embed.set_image(url = "https://cdn.discordapp.com/attachments/712825742253359105/729442017037516800/boutiqueee.png")
            embed.set_footer(text = "Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous n'avez pas entré de paramètre valide. (`bannieres`, `titres`, `divers`)"
            ))

    @commands.command(aliases = ['edit-shop', 'edit-shop-item'])
    async def edit_shop(self, ctx, param, name, param2, value):
        with open("cogs/items.json", "r") as f:
            items = json.load(f)
        if param == "banner" or param == "banniere":
            if name in items["shop"]["banners"].keys():
                if param2 == "value" or param2 == "desc" or param2 == "description":
                    items["shop"]["banners"][name]["desc"] = value
                    await ctx.send(f"Vous avez bien changé la description de la bannière {name} en ```{value}```")
                elif param2 == "price" or param2 == "prix":
                    items["shop"]["banners"][name]["price"] = int(value)
                    await ctx.send(f"Vous avez bien changé le prix de la bannière {name} à **{value}** Magic Coins.")
            else:
                await ctx.send(embed = await error_embed(
                error = "La bannière mise n'existe pas ou n'est pas vendue dans le shop."
            ))
        elif param == "titre" or param == "title":
            if name in items["shop"]["titles"].keys():
                if param2 == "value" or param2 == "desc" or param2 == "description":
                    items["shop"]["titles"][name]["desc"] = value
                    await ctx.send(f"Vous avez bien changé la description du titre {name} en ```{value}```")
                elif param2 == "price" or param2 == "prix":
                    items["shop"]["titles"][name]["price"] = int(value)
                    await ctx.send(f"Vous avez bien changé le prix du titre {name} à **{value}** Magic Coins.")
            else:
                await ctx.send(embed = await error_embed(
                error = "Le titre mis n'existe pas ou n'est pas vendu dans le shop."
            ))
        else:
            await ctx.send(embed = await error_embed(
                error = "Vous n'avez pas entré de paramètre valide. (`banner`, `title`)"
            ))
        with open("cogs/items.json", "w") as f:
            json.dump(items, f, indent = 4)


def setup(bot):
    bot.add_cog(Economy(bot))