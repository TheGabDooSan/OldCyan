import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.gold(),
            title = f"{ctx.guild.name} | Help",
            description = "Affiche les commandes disponibles sur le serveur."
        )
        if ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            embed.add_field(
                name = "Game Masters",
                value = "`admin-edit <param> <member> <value>`, `create-banner <name> <type> <rarity>`, `create-title <name> <value>`, `delete-banner <name>`, `delete-title <name>`, `give banner/title <member> <name>`, `set <guild> <param> <value>`, `take banner/title <member> <name>`, `embed-image <url>`, `kick_self`, `serverlist`, `hourly-msg <work/battle/crime> [<message>]`, `hourly-gain <min> <max> [<work/battle/crime>]`",
                inline = False
            )
        if ctx.author.guild_permissions.administrator or ctx.author.id == 274558756522557440 or ctx.author.id == 707402860853329931:
            embed.add_field(
                name = "<a:hypeshiny:725355352610177046> - **__Server Admin__**",
                value = "`embed <text>`, `say <text>`, `clear <nmb_msg>`, `image <url>`, `voice-connect`",
                inline = False
            )
        embed.add_field(name = "<a:689892675369041980:725355483631845477> - **__Profiles commandes__**",
                        value = "`register`, `profile [<member>]`, `edit <desc/friend> <value>`, `rep <member>`, `alliance <member>`, `divorce`, `inv [<member>]`, `use <banner/title> <name>`",
                        inline = False)
        embed.add_field(name = "<:14:716321702702874754> - **__Guildes et World Boss__**",
                        value = "`boss_info`, `rollboss <lvl>`, `guilde <name>`",
                        inline = False)
        embed.add_field(name = "<a:MagicCoins:728621926809075732> - **__Economie__**",
                        value = "`work`, `battle`, `crime`, `balance [<member>]`, `give-money <member> <amount>`",
                        inline = False)
        embed.add_field(name = "<a:E1:722886843430862981> - **__Boutique__**",
                        value = "`shop <banners/titles>`, `buy <banner/title> <name>`, `banners-list`, `titles-list`, `banner-info <name>`, `title-info <name>`",
                        inline = False)
        embed.add_field(name = "<a:earth:717102964287865024> - **__Utilitaire__**",
                        value = "`hug [<member>]`, `kiss [<member>]`, `slap [<member>]`, `server-info`, `roll <nmb>`, `version`, `support`",
                        inline = False)
        embed.set_author(name = ctx.message.author.name)
        embed.set_footer(text = ctx.guild.name)
        embed.set_image(url = "https://gifimage.net/wp-content/uploads/2018/05/show-by-rock-cyan-gif-3.gif")

        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Help(bot))
