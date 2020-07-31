import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, MissingPermissions, MissingRequiredArgument, CommandNotFound, UserInputError, BotMissingPermissions, BadArgument
from main import error_embed, bot_prefix

import datetime

class CommandErrors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        ignored = CommandNotFound
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return
        
        elif isinstance(error, MissingPermissions):
            return await ctx.send(embed = await error_embed(
                error_name = "MissingPermissions",
                error = "Vous n'avez pas la permission requise pour executer cette commande."
            ))
        
        elif isinstance(error, BotMissingPermissions):
            return await ctx.send(embed = await error_embed(
                error_name = "BotMissingPermissions",
                error = "Le bot n'a pas la permission requise pour executer cette commande."
            ))

        elif isinstance(error, (BadArgument, UserInputError)):
            return await ctx.send(embed = await error_embed(
                error_name = "BadArgument | UserInputError",
                error = "Vous n'avez pas utilisé la commande de la bonne façon."
            ))

        elif isinstance(error, CommandOnCooldown):
            if error.retry_after > 60:
                return await ctx.send(embed = await error_embed(
                    error_name = "CommandOnCooldown",
                    error = f"Attendez **{error.retry_after / 60:.0f}**min avant de pouvoir refaire cette commande."
                ))
            elif error.retry_after < 61:
                return await ctx.send(embed = await error_embed(
                    error_name = "CommandOnCooldown",
                    error = f"Attendez **{error.retry_after:.0f}**s avant de pouvoir refaire cette commande."
                ))


def setup(bot):
    bot.add_cog(CommandErrors(bot))