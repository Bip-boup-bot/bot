from nextcord.ext import commands
from nextcord import Member
from language import translate, load
class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = self.client = bot
  
  @commands.command()
  async def ban(self, ctx, member: Member = None, *, reason: str = None):
    langu: str = load(ctx.author.id)
    if not any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])).lower() for word in ['ban']): return await ctx.send(translate('missingperm', langu))
    if member is None: return await ctx.send(translate('missingping', langu).format("ban"))
    ban = translate('ban', langu).format(ctx.author.name, member.name) + f'\n{reason}' if reason is not None else ""
    try:
      await member.send(ban)
    except:
      pass
    try:
      await member.ban(reason=ban)
    except:
      return await ctx.send(translate('botmissingperm', langu))
    await ctx.send(ban)
    del ban

  @commands.command()
  async def kick(self, ctx, member: Member = None, *, reason: str = None):
    langu: str = load(ctx.author.id)
    if not any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])).lower() for word in ['kick']): return await ctx.send(translate('missingperm', langu))
    if member is None: return await ctx.send(translate('missingping', langu).format("kick"))
    kick = translate('kick', langu).format(ctx.author.name, member.name) + f'\n{reason}' if reason is not None else ""
    try:
      await member.send(kick)
    except:
      pass
    try:
      await member.kick(reason=kick)
    except:
      return await ctx.send(translate('botmissingperm', langu))
    await ctx.send(kick)
    del kick

def setup(bot):
  bot.add_cog(Moderation(bot))
