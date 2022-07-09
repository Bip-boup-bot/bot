from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=['?'], help_command=None, intents=Intents.all())
from os import listdir, environ
for i in listdir('cogs'):
  if i.endswith('.py'):
    bot.load_extension(f'cogs.{i[: -3]}')
bot.run(environ['token'])
