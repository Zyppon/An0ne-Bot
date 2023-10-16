import disnake
from disnake.ext import commands
import os
#from discord.utils import find

dir_path = 'cogs'

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='>' , intents=intents ,  help_command=None)

@bot.event

async def on_ready():
    print(f"Logged in {bot.user.name}")
    print(f"Bot is on {len(bot.guilds)} servers:")
    for guild in bot.guilds:
         print(f"- {guild.name} ({guild.id})")
    
@bot.event
async def on_guild_join(guild):
    for text_channel in guild.text_channels:
        if text_channel.name == 'general':
            embed = disnake.Embed(
            title="Hello, Thanks for adding me to this server!",
            description="An0ne Bot, your Discord server companion. My command prefix is ​​>, so when you want to use a command, you have to start the message with >. As an An0ne bot, I offer a variety of features that focus on anonymity and privacy. You have anonymous chat channels, anonymous reporting options, and other ways to keep your identity safe. If you want to know more about me or find useful resources, you can visit my official page: Link to An0ne page. With me on board, you'll experience a safer and more creative experience on your Discord server. Welcome to the world of An0ne! \n ***Make sure you give me the necessary permissions to use the commands***",
            color=disnake.Colour.green(),
            )
          #  embed.set_thumbnail(url="")
            await text_channel.send(embed=embed)
            print(f"The bot has been added on {guild.name}")
try:   
   for filename in os.listdir(dir_path):
    if filename.endswith('.py'):
        cogs = filename[:-3]
        bot.load_extension(f"{dir_path}.{cogs}")   
except FileNotFoundError:
    print(f"Make sure you verified the cogs folder")
  
  
    
if __name__ == "__main__":
    bot.run("TOKEN")
else:
    print(f"Error expected , try to run from main file.")