import nextcord
from nextcord.ext import commands
from Config import Token # import ur Token
intents = nextcord.Intents.default() # without these lines, the bot will work, but will not respond to messages
intents.message_content = True

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from nextcord.ext import commands
bot = commands.Bot(command_prefix='!', intents=intents) # here a prefix is set so that the bot understands the beginning of the command, prefixes can be set almost any


@bot.event
async def on_ready(): # lets you know that the bot has earned
    print(f'Врубился малыш {bot.user}')

@bot.command() 
async def команды(interaction: nextcord.Interaction): # the usual command that outputs text
    await interaction.send("`!привет`\n`!ролл за мид`\n`!профиль`\n`!удалить`")

@bot.command(pass_context=True) # command to delete messages, this command deletes amount of messages + 1 (the command itself sent)
async def удалить(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)


bot.run(Token)