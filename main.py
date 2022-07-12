from nextcord.ext import commands
from nextcord import Intents
from threading import Thread
bot = commands.Bot(command_prefix=['?'], help_command=None, intents=Intents.all())
from os import listdir, environ, system
for i in listdir('cogs'):
  if i.endswith('.py'):
    def hi():
      bot.load_extension(f'cogs.{i[: -3]}')
    t = Thread(target=hi)
    t.start()
bot.run(environ['token'])
