import discord
from discord.ext import commands
from discord.utils import get

class Listeners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        name = member.mention
        channel = get(member.guild.channels, id = 707247334391545897)  # ID : 707064288715472968

        await channel.send("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                           "<a:E7:722891236922490990> ❦ ►█▓▒░█░░▒▒▓█▒░ <a:E27:722912864033177750>**__❦EPHEDIA❦__**<a:E28:722912873868689540>  ░▒█▓▒▒░░█░▒▓█◄ ❦<a:E7:722891236922490990>\n"
                           "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
                           "֎ ║<a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> <a:710004888536350741:722923208445263923> ║ ֎\n"
                           "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                           "║ <a:721206995176390676:722923273175826463> **__❦ ►Bienvenue à toi {} <a:721206995176390676:722923273175826463> ◄ ❦__**\n"
                           "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
                           "║ <a:E23:722912815333244970> **__❦ ►Nous sommes désormais {} sur le serveur !◄ ❦__**<a:E23:722912815333244970>\n"
                           "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                           "║ <a:E5:722887534060896388> **__❦ ►Nous vous invitons à regarder le règlement du serveur ◄ ❦__** #📜⌠règlements⌡꧂ \n"
                           "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
                           "║<a:E7:722891236922490990> **__❦ ►L'équipe d'éphédia vous souhaite un agréable séjour parmis nous !◄ ❦__**\n"
                           "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                           "║<a:710004888536350741:722923208445263923> https://i.kym-cdn.com/photos/images/newsfeed/001/004/296/162.gif <a:710004888536350741:722923208445263923>\n"
                           "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█".format(name, str(len(member.guild.members))))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        name = member.name
        channel = get(member.guild.channels, id = 707247334391545897)  # ID : 707064288715472968

        await channel.send("{} **__a  quitté le serveur, quel dommage, 1 de perdu 10 de retrouvé <:20:714630072786485265> __**".format(name))

    @commands.Cog.listener()
    async def on_message(self, message):

        A = "<a:E9:722891271504396388>" # E9
        B = "<a:710004888536350741:722923208445263923>" # 710004888536350741
        C = "<a:716785945717768273:723013461612953601>" # 716785945717768273
        D = "<a:652438428788588544:723013400598151208>" # 652438428788588544
        E = "<a:E7:722891236922490990>" # E7
        F = "<a:710004866482962432:722923127339745372>" # 710004866482962432
        G = "<a:E12:722891301711904850>" # E12
        H = "<a:702698343200981012:723013427353616406>" # 702698343200981012
        I = "<a:702698343767212122:723013435809333269>" # 702698343767212122
        J = "<a:721206995176390676:722923273175826463>" # 721206995176390676

        channel = message.channel
        if message.content == f"{B}{A}{B}{C} **__❦ Nous sommes de retour ❦__** {C}{B}{A}{B}":
            await channel.send(f"{A}{B}{A}{D} **__❦ Pour vous jouer un mauvais tour ! ❦__** {D}{A}{B}{A}")

        if message.content == f"{B} {A}{B}{E}   **__❦ Afin de préserver discord de la dévastation ! ❦__** {E}  {B}  {A}{B}":
            await channel.send(f"{A}{B}{A} {F}  **__❦ Afin de rallier les serveurs dans notres nations ! ❦__** {F}   {A}{B}{A}")

        if message.content == f"{B} {A}{B} {G}  **__❦ Afin d'écraser l'hypocrie et l'idiocité ! ❦__** {G}  {B}  {A}{B}":
            await channel.send(f"{A}{B}{A} {G}  **__❦ Afin d'étendre de répendre nos pailletes jusqu'à la voie lactée ! ❦__** {G}  {A}{B}{A}")

        if message.content == f"{B} {A}{B}{C}  **__❦ Je suis Kayla ! ❦__** {C} {B}  {A}{B}":
            await channel.send(f"{A}{B}{A} {C}  **__❦ Et moi Ephédia ! ❦__** {C} {A}{B}{A}")

        if message.content == f"{B}  {A}{B}  {J} **__❦ La team Paillette plus rapide que la lumière ! ❦__** {J} {B}  {A}{B}":
            await channel.send(f"{A}{B}{A} {H} **__❦ Rendez vous tous, ou ça sera la guerre ! ❦__** {H} {A}{B}{A}")

        if message.content == f"{B}  {A}{B}  {I}  **__❦ OUI LA GUERRE ! ❦__** {I} {B}  {A}{B}":
            embed = discord.Embed(
                colour = discord.Colour(0x6e1faf)
            )
            embed.set_image(url = "https://i.kym-cdn.com/photos/images/newsfeed/001/004/296/162.gif")
            await channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Listeners(bot))