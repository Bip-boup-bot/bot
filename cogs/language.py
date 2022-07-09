from nextcord.ext import commands
from language import boutton
class Language(commands.Cog):
  def __init__(self, bot):
    self.bot = self.client = bot
  
  @commands.command()
  async def language(self, ctx):
    view = boutton()
    await ctx.send("Choose the language", view=view)
    await view.wait()

def setup(bot):
  bot.add_cog(Language(bot))
