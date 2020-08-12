import discord
from discord.ext import commands
from discord.utils import get
from main import randcolour, error_embed

import asyncio
import json


class Profiles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['profil', 'p'])
    async def profile(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        with open('cogs/profile.json', 'r') as f:
            profiles_file = json.load(f)
            get_profile = profiles_file[str(member.id)]
        with open('cogs/items.json', 'r') as f:
            items = json.load(f)
        if str(member.id) in profiles_file.keys():

            def get_guild():
                ephedia_guild = self.bot.get_guild(707063500903678023)
                ephedia_member = ephedia_guild.get_member(member.id)
                divinity = get(ephedia_guild.roles, id=707727361927413802)
                calix = get(ephedia_guild.roles, id=707726324449411112)
                volta = get(ephedia_guild.roles, id=707726328652365875)
                xeris = get(ephedia_guild.roles, id=707726330388807721)
                borealise = get(ephedia_guild.roles, id=707726326232252478)
                ephedia = get(ephedia_guild.roles, id=707726332137832558)
                if ephedia_member is not None:
                    if divinity in ephedia_member.roles:
                        return divinity.name
                    elif calix in ephedia_member.roles:
                        return calix.name
                    elif volta in ephedia_member.roles:
                        return volta.name
                    elif xeris in ephedia_member.roles:
                        return xeris.name
                    elif borealise in ephedia_member.roles:
                        return borealise.name
                    elif ephedia in ephedia_member.roles:
                        return ephedia.name
                    else:
                        return "Aucune guilde"
                else:
                    return "Rejoignez Ephedia"

            def get_vip_level():
                ephedia_guild = self.bot.get_guild(707063500903678023)
                ephedia_member = ephedia_guild.get_member(member.id)
                vip1 = get(ephedia_guild.roles, id=707251593308799057)
                vip2 = get(ephedia_guild.roles, id=707252007223951360)
                vip3 = get(ephedia_guild.roles, id=707252084159938600)
                vip4 = get(ephedia_guild.roles, id=707252164346642583)
                vip5 = get(ephedia_guild.roles, id=707252360681881700)
                vip6 = get(ephedia_guild.roles, id=707252426520133633)
                vip7 = get(ephedia_guild.roles, id=707252500973223947)
                vip8 = get(ephedia_guild.roles, id=707252568547393626)
                
                if ephedia_member is not None:
                    if vip1 in ephedia_member.roles:
                        return vip1.name
                    elif vip2 in ephedia_member.roles:
                        return vip2.name
                    elif vip3 in ephedia_member.roles:
                        return vip3.name
                    elif vip4 in ephedia_member.roles:
                        return vip4.name
                    elif vip5 in ephedia_member.roles:
                        return vip5.name
                    elif vip6 in ephedia_member.roles:
                        return vip6.name
                    elif vip7 in ephedia_member.roles:
                        return vip7.name
                    elif vip8 in ephedia_member.roles:
                        return vip8.name
                    else:
                        return "Non vip"
                else:
                    return "Rejoingnez Ephedia"
            
            def get_succes():
                succes = 0
                for banner in list(items['banners'].keys()):
                    if banner in profiles_file[str(member.id)]['inv']['banners']:
                        if items['banners'][banner]['type'] == "C":
                            succes += 500
                        if items['banners'][banner]['type'] == "B":
                            succes += 1499
                        if items['banners'][banner]['type'] == "A":
                            succes += 2999
                        if items['banners'][banner]['type'] == "S":
                            succes += 4750
                        if items['banners'][banner]['type'] == "Z":
                            succes += 7500
                for title in list(items['titles'].keys()):
                    if title in profiles_file[str(member.id)]['inv']['titles']:
                        succes += 25
                return succes

            embed = discord.Embed(
                title=f"Profile",
                description=f"Voici le profil de {member.name}\n"
                "\n"
                f"<a:hypeshiny:725355352610177046> **Pseudo** : {member.mention}\n"
                f"<a:706138548457177128:722923174718734406> **Titre** : {get_profile['titre']}\n"
                f"<a:689892675369041980:725355483631845477> **Description** : {get_profile['desc']}\n"
                "\n"
                f"<a:MagicCoins:728621926809075732> **MagicCoins** : {get_profile['balance']}\n"
                "\n"
                f"<a:E4:722887481145688166> **Club VIP** : ``{get_vip_level()}``\n"
                f"<a:4147_magical_heart:722852234072686672> **Guilde** : ``{get_guild()}``\n"
                "\n"
                f"<a:E2:722887411641614387> **Meilleur(e) Ami(e)** : {get_profile['best_friends']}\n"
                f"<a:E19:722912770785542259> **Conjoin(te)** : {get_profile['partner']}\n"
                "\n"
                f"<a:E9:722891271504396388> **Succès** : {get_succes()}\n"
                f"<a:E21:722912788397293600> **Badges** : {get_profile['badges']}\n"
                "\n"
                f"<a:724298797001343007:725355678276780032> **Popularité** : {get_profile['rep']}\n",
                colour=randcolour()
            )
            embed.set_footer(text="Ⓒ 2020 EPHEDIA FR. TOUS DROITS RÉSERVÉS.")
            embed.set_thumbnail(url=member.avatar_url)
            if get_profile['image'] is not None:
                embed.set_image(url=get_profile['image'])

            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=await error_embed(
                error="Vous devez d'abord vous enregistrer avec `:!register`"
            ))

    @commands.command()
    async def edit(self, ctx, param: str, *, value):
        with open('cogs/profile.json', 'r') as f:
            profiles_file = json.load(f)
        if not param or not value:
            await ctx.send(embed=await error_embed(
                error="Veuillez spécfier un paramètre et une valeur."
            ))
        elif param == "desc" or param == "description":
            param = "desc"
            profiles_file[str(ctx.author.id)]['desc'] = value
            with open('cogs/profile.json', 'w') as f:
                json.dump(profiles_file, f, indent=4)
            embed = discord.Embed(
                colour=randcolour(),
                description=f"Vous avez changé votre description en : ```{profiles_file[str(ctx.author.id)]['desc']}```"
            )
            await ctx.message.delete()
            await ctx.send(embed=embed)
        elif param == "best_friends" or param == "friends" or param == "friend":
            param = "best_friends"
            value = value.split(" ")
            profiles_file[str(ctx.author.id)]['best_friends'] = value[0]
            with open('cogs/profile.json', 'w') as f:
                json.dump(profiles_file, f, indent=4)
            embed = discord.Embed(
                colour=randcolour(),
                description=f"Vous avez changé votre meilleur ami en : ' {profiles_file[str(ctx.author.id)]['best_friends']} '"
            )
            await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=await error_embed(
                error="Veuillez spécifier un paramètre valide."
            ))

    @commands.command(aliases=['reputation', 'reput'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def rep(self, ctx, member: discord.Member = None):
        if member is not None:
            if member.id != ctx.author.id:
                with open("cogs/profile.json", "r") as f:
                    profiles_file = json.load(f)
                if str(ctx.author.id) in profiles_file.keys():
                    if str(member.id) in profiles_file.keys():
                        embed = discord.Embed(
                            title="Réputation",
                            colour=randcolour(),
                            description=f"{ctx.author.mention} donne un point de réputation a {member.mention}"
                        )
                        profiles_file[str(member.id)]['rep'] += 1
                        with open("cogs/profile.json", "w") as f:
                            json.dump(profiles_file, f, indent=4)
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(embed=await error_embed(
                            error=f"{member.mention} doit d'abord s'enregistrer pour recevoir un point de réputation ! (`:!register`)"
                        ))
                        ctx.command.reset_cooldown(ctx)
                else:
                    await ctx.send(embed=await error_embed(
                        error=f"Vous devez d'abord vous enregistrer pour donner un point de réputation ! (`:!register`)"
                    ))
                    ctx.command.reset_cooldown(ctx)
            else:
                await ctx.send(embed=await error_embed(
                    error="Vous ne pouvez pas vous donner un point de réputation."
                ))
                ctx.command.reset_cooldown(ctx)
        else:
            await ctx.send(embed=await error_embed(
                error="Vous devez spécifier quelqu'un."
            ))
            ctx.command.reset_cooldown(ctx)

    @commands.command()
    async def register(self, ctx):
        with open("cogs/profile.json", "r") as f:
            profiles_file = json.load(f)
        m = str(ctx.author.id)
        if m not in profiles_file.keys():
            profiles_file[m] = {}
            profiles_file[m]["titre"] = "Aucun titre"
            profiles_file[m]["desc"] = "Aucune description"
            profiles_file[m]["best_friends"] = "Aucun(e) meilleur(e) ami(e)"
            profiles_file[m]["partner"] = "Aucun(e) conjoint(e)"
            profiles_file[m]["partner_id"] = None
            profiles_file[m]["badges"] = "Aucun badge"
            profiles_file[m]["succes"] = "0"
            profiles_file[m]["image"] = None
            profiles_file[m]["rep"] = 0
            profiles_file[m]["anim_rep"] = 0
            profiles_file[m]["inv"] = {"banners": [], "titles": []}
            profiles_file[m]["balance"] = 0

            with open("cogs/profile.json", "w") as f:
                json.dump(profiles_file, f, indent=4)

            await ctx.send("Vous avez bien été enregistré ! Tappez la commande `:!profile` pour voir votre profil.")
            print(f"New profile ! [{ctx.author.name}]")
        else:
            await ctx.send("Vous êtes déja enregistré. Tappez la commande `:!profile`")

    @commands.command(aliases=['mary', 'aliance'])
    async def alliance(self, ctx, member: discord.Member = None):
        ephedia = self.bot.get_guild(id=707063500903678023)
        author = ephedia.get_member(ctx.author.id)
        user = ephedia.get_member(member.id)
        role = get(ephedia.roles, id=726227013337350214)
        if ctx.author in ephedia.members and member in ephedia.members:
            if role in author.roles:
                if not member.bot or ctx.author.id != member.id:
                    with open("cogs/profile.json", "r") as f:
                        profiles_file = json.load(f)
                    if str(ctx.author.id) in profiles_file.keys():
                        if str(member.id) in profiles_file.keys():
                            if profiles_file[str(member.id)]['partner_id'] is None:
                                embed = discord.Embed(
                                    title="Demande en mariage",
                                    colour=randcolour(),
                                    description=f"{member.mention}, voulez-vous prendre {ctx.author.name} comme épou(x/se) ? \n(__OUI__ / __NON__)"
                                )
                                embed.set_footer(text="Expiration dans 3min")
                                await ctx.send(embed=embed)

                                def check(m):
                                    return m.channel == ctx.channel and m.target == member

                                try:
                                    msg = await self.bot.wait_for('message', timeout=180, check=lambda message: message.author == member and message.channel == ctx.channel)
                                    if msg.content.lower() == "OUI" or msg.content.lower() == "Oui" or msg.content.lower() == "oui":
                                        profiles_file[str(
                                            member.id)]['partner'] = ctx.author.mention
                                        profiles_file[str(member.id)]['partner_id'] = str(
                                            ctx.author.id)
                                        profiles_file[str(
                                            ctx.author.id)]['partner'] = member.mention
                                        profiles_file[str(ctx.author.id)]['partner_id'] = str(
                                            member.id)
                                        with open("cogs/profile.json", "w") as f:
                                            json.dump(
                                                profiles_file, f, indent=4)
                                        await author.remove_roles(role)
                                        await ctx.send(f"Félicitations ! {member.mention} et {ctx.author.mention} sont désormais mariés !")
                                    elif msg.content.lower() == "NON" or msg.content.lower() == "Non" or msg.content.lower() == "non":
                                        await ctx.send(f"Désolé {ctx.author.mention}, mais ta demande de mariage a été refusée :/")
                                except asyncio.TimeoutError:
                                    await ctx.send("Votre demande en mariage a expirée, ce sera pour une autre fois...")
                            else:
                                await ctx.send(embed=await error_embed(
                                    error="Vous et/ou la personne que vous demandez en mariage est déjà marié(e).\nContactez un administrateur si vous pensez que c'est une erreur."
                                ))
                        else:
                            await ctx.send(embed=await error_embed(
                                error=f"{member.mention} ne s'est pas encore enregistré (`:!register`)."
                            ))
                    else:
                        await ctx.send(embed=await error_embed(
                            error="Vous devez d'abord vous enregistrer avant d'executer cette commande, `:!register`"
                        ))

                else:
                    await ctx.send(embed=await error_embed(
                        error=f"Vous ne pouvez pas vous marrier avec {member.mention}"
                    ))
            else:
                await ctx.send(embed=await error_embed(
                    error=f"Il vous manque une {role.name} pour pouvoir vous marrier ;p"
                ))
        else:
            await ctx.send(embed=await error_embed(
                error="Vous ou le/la marié(e) devez avoir rejoint le serveur principal pour vous marier. ([Invite](https://discord.gg/w7kWcjV))"
            ))

    @commands.command()
    async def divorce(self, ctx):
        with open("cogs/profile.json", "r") as f:
            profiles_file = json.load(f)
        if profiles_file[str(ctx.author.id)]['partner_id'] is not None:
            await ctx.send(f"Suite a une dispute, {ctx.author.mention} décide de divorcer avec {profiles_file[str(ctx.author.id)]['partner']} \:'(")
            partner_id = profiles_file[str(ctx.author.id)]['partner_id']
            profiles_file[str(ctx.author.id)
                          ]['partner'] = "Aucun(e) conjoint(e)"
            profiles_file[str(ctx.author.id)]['partner_id'] = None
            profiles_file[partner_id]['partner'] = "Aucun(e) conjoint(e)"
            profiles_file[partner_id]['partner_id'] = None
            with open("cogs/profile.json", "w") as f:
                json.dump(profiles_file, f, indent=4)
        else:
            await ctx.send(embed=await error_embed(
                error="Vous n'êtes pas marié."
            ))

    @commands.command(aliases=['admin_edit', 'cm_edit', 'admin-edit', 'cm-edit'])
    async def adminedit(self, ctx, member: discord.Member = None, param=None, *, value=None):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            if param is None:
                await ctx.send(embed=await error_embed(
                    error="Vous devez spécifier un paramètre a modifier"
                ))
            if param == "titre" or param == "title" or param == "desc" or param == "friends" or param == "best_friends" or param == "partner" or param == "vip" or param == "clubvip" or param == "succes" or param == "badges" or param == "badge" or param == "guilde" or param == "guild" or param == "image":
                if value is None:
                    await ctx.send(embed=await error_embed(
                        error=f"Vous devez donner une valeur au paramètre `{param}`."
                    ))
                else:
                    with open('cogs/profile.json', 'r') as f:
                        profiles_file = json.load(f)

                    if param == "friends":
                        param = "best_friends"

                    if param == "title":
                        param = "titre"

                    if param == "clubvip":
                        param = "vip"

                    if param == "badge":
                        param = "badges"

                    if param == "guilde":
                        param = "guild"

                    if param == "description":
                        param = "desc"

                    profiles_file[str(member.id)][param] = value

                    with open('cogs/profile.json', 'w') as f:
                        json.dump(profiles_file, f, indent=4)

                    def result_msg(param, member):
                        if param == "titre":
                            return "Vous avez modifié votre titre en :\n"
                        elif param == "guild":
                            return f"Vous avez modifié la guilde de {member.mention} en :\n"
                        elif param == "desc":
                            return f"Vous avez changé la description de {member.mention} en :\n"
                        elif param == "best_friends":
                            return f"Vous avez modifié la liste des meilleur(e)(s) ami(e)(s) de {member.mention} en :\n"
                        elif param == "partner":
                            return f"Vous avez changé le conjoint de {member.mention} avec :\n"
                        elif param == "vip" or param == "clubvip":
                            return f"Le status VIP de {member.mention} a été changé en :\n"
                        elif param == "succes":
                            return f"Les succes de {member.mention} ont été changés en :\n"
                        elif param == "badges":
                            return f"Les badges de {member.mention} ont été modifiés en :\n"
                        elif param == "image":
                            return f"L'image du membre {member.mention} a été changée en : \n"

                    embed = discord.Embed(
                        colour=randcolour(),
                        description=f"{result_msg(param, member)}{profiles_file[str(member.id)][param]}"
                    )
                    await ctx.message.delete()
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=await error_embed(
                    error=f"Le paramètre `{param}` n'existe pas."
                ))
        else:
            await ctx.send(embed=await error_embed(
                error_name="MissingPermissions",
                error="Vous n'avez pas la permission d'executer cette commande."
            ))

    @commands.command(aliases = ['top', 'lead'])
    async def leaderboard(self, ctx):
        with open("cogs/profile.json", "r") as f:
            profiles = json.load(f)
        def maximum(iterable, n = 10):
            out = []
            it = iterable[:]
            while it and len(out) < 10:
                out.append(it.pop(it.index(max(it))))
            return out
        balances = []
        names = []
        for profile in profiles:
            balances.append(profiles[profile]['balance'])
            names.append(profiles[profile])
        embed = discord.Embed(
            colour = randcolour(),
        )
        for bal in maximum(balances):
            embed.add_field(name = "** **", value = f"<@> - <a:MagicCoins:728621926809075732>{bal}", inline = False)
        await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(Profiles(bot))
