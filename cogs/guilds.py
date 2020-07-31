import discord
from discord.ext import commands
from discord.utils import get
from main import error_embed, randcolour

import json

class Guilds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def set_value(self, guild, param, value):
        with open('cogs/guilds.json', 'r') as f:
            guilds_file = json.load(f)
        if param == "contrib":
            value = int(value)
        guilds_file['guilds'][guild][param] = value

        with open('cogs/guilds.json', 'w') as f:
            json.dump(guilds_file, f, indent = 4)

    @commands.command(aliases = ['guilds', 'guild', 'guild_info', 'guilde_info'])
    async def guilde(self, ctx, guild: str):
        if not guild:
            await ctx.send(embed = await error_embed(
                error = "Vous devez spécifier une guilde."
            ))

        elif guild == "xeris" or guild == "Xeris":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['xeris']

        elif guild == "calix" or guild == "Calix":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['calix']

        elif guild == "ephedia" or guild == "Ephedia":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['ephedia']

        elif guild == "divinity" or guild == "Divinity":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['divinity']

        elif guild == "borealise" or guild == "Borealise":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['borealise']

        elif guild == "volta" or guild == "Volta":
            with open('cogs/guilds.json', 'r') as f:
                guilds_file = json.load(f)
            get_guild = guilds_file['guilds']['volta']

        else:
            await ctx.send(embed = await error_embed(
                error = f"La guilde `{guild}` n'existe pas."
            ))

        def guild_member_count(guild):
            counter = 0
            divinity = get(ctx.guild.roles, id = 707727361927413802)
            calix = get(ctx.guild.roles, id = 707726324449411112)
            volta = get(ctx.guild.roles, id = 707726328652365875)
            xeris = get(ctx.guild.roles, id = 707726330388807721)
            borealise = get(ctx.guild.roles, id = 707726326232252478)
            ephedia = get(ctx.guild.roles, id = 707726332137832558)
            for member in ctx.guild.members:
                if guild == "calix" or guild == "Calix":
                    if calix in member.roles:
                        counter += 1
                elif guild == "divinity" or guild == "Divinity":
                    if divinity in member.roles:
                        counter += 1
                elif guild == "volta" or guild == "Volta":
                    if volta in member.roles:
                        counter +=1
                elif guild == "xeris" or guild == "Xeris":
                    if xeris in member.roles:
                        counter += 1
                elif guild == "borealise" or guild == "Borealise":
                    if borealise in member.roles:
                        counter += 1
                elif guild == "ephedia" or guild == "Ephedia":
                    if ephedia in member.roles:
                        counter += 1
            return str(counter)


        embed = discord.Embed(
            colour = randcolour(),
            title = "Guilde",
            description = f"Voici des informations concernant la guilde {get_guild['name']} :"
        )
        embed.add_field(
            name = "Nom de la guilde :",
            value = get_guild['name'], inline = False
        )
        embed.add_field(
            name = "Chef / Gérant :",
            value = get_guild['leader'], inline = False
        )
        embed.add_field(
            name = "Niveau :",
            value = get_guild['level'], inline = False
        )
        embed.add_field(
            name = "Contribution :",
            value = f"{get_guild['contrib']}/{get_guild['contriblvl']}", inline = False
        )
        embed.add_field(
            name = "Badges :",
            value = get_guild['badges'], inline = False
        )
        embed.add_field(
            name = "Nombre de membres :",
            value = f"{guild_member_count(guild)} membres", inline = False
        )
        embed.set_footer(text = ctx.guild.name)

        if get_guild['image'] is not None:
            embed.set_image(url = get_guild['image'])

        await ctx.send(embed = embed)

    @commands.command()
    async def set(self, ctx, guild, param, *, value):
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            if param == "name" or param == "contrib" or param == "image" or param == "thumb" or param == "contriblvl" or param == "level" or param == "lvl" or param == "leader" or param == "badges": 
                self.set_value(
                    guild = guild,
                    param = param,
                    value = value
                )
                
                embed = discord.Embed(
                    colour = randcolour(),
                    description = f"Nouvelle valeur pour ce paramètre changée avec succès.\n({param} = {value})"
                )

                await ctx.send(embed = embed)
            else:
                await ctx.send(embed = await error_embed(
                    error_name = "BadArgument",
                    error = "Vous n'avez pas utilisé le bon paramètre."
                ))
        else:
            await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission d'executer cette commande."
            ))


def setup(bot):
    bot.add_cog(Guilds(bot))