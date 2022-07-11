from nextcord.ext import commands
from language import translate, load
from namedb import edit, get, search, add
from nextcord import Embed
class Todo(commands.Cog):
  def __init__(self, bot):
    self.bot = self.client = bot

  @commands.command()
  async def todo(self, ctx, action: str = "display", num = None, *, value: str = None):
    langu: str = load(ctx.author.id)
    e: str = str(ctx.author.id)
    if action == "display":
      try:
        elements: list = get(e, categorie="todo")
      except:
        return await ctx.send(translate('nolist', langu))
      desc: str = ''
      for i in range(len(elements)):
        desc += f'\n**{i + 1}**. {elements[i]}'
      await ctx.send(embed=Embed(title=f"**{ctx.author.name}** Todolist", description=desc, color=0x3498db))
    elif action == "add":
      val: str = num + " " + value
      if search(e, categorie="todo") is True:
        p = get(e, categorie='todo')
        p.append(val)
        edit(e, p, categorie="todo")
      else:
        add(e, [val], categorie="todo")
      await ctx.send(translate("add", langu).format(val))
    elif action == 'remove':
      val = get(e, categorie="todo")
      try:
        del val[int(num) - 1]
      except:
        return await ctx.send(translate("valueerror", langu))
      edit(e, val, categorie="todo")
    else:
      await ctx.send(translate("invalidtype", langu).format("action", "actions", "\nadd\ndisplay\nremove"))

def setup(bot):
  bot.add_cog(Todo(bot))
