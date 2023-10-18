import sys
import traceback

import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Logged in {bot.user.name}")
    print(f"Bot is on {len(bot.guilds)} servers:")
    for guild in bot.guilds:
        print(f"- {guild.name} ({guild.id})")


@bot.event
async def on_guild_join(guild):
    for text_channel in guild.text_channels:
        if text_channel.name == "general":
            embed = disnake.Embed(
                title="Hello, Thanks for adding me to this server!",
                description="Meet An0ne Bot, your trusty Discord server protector. My command prefix is `>`, "
                "so when you want to use a command, you have to start the message with >."
                "As your dedicated moderation bot, I'm here to help maintain order"
                "\t\n**Key Features:**"
                "\n**User Management:** I assist in member verification, role assignment, and monitoring new member activities."
                "\n**Message Filtering and Moderation:** My automated filters keep an eye out for inappropriate content and"
                "rule violations, allowing me to issue warnings and remove offending messages."
                "\n**Warning System:** I can issue warnings to rule violators, keep track of them,"
                "and apply appropriate sanctions such as timeouts or bans."
                "\n**Link and Attachment Filtering:** I help prevent spam and protect against harmful content"
                "by monitoring and filtering links and attachments."
                "\nReporting System: I provide a user-friendly system for reporting abuse or rule violations,"
                "ensuring timely response from server moderators."
                "\n**Automatic Inappropriate Content Detection:** I'm equipped to automatically identify" 
                "and take action against inappropriate content, like NSFW images or vulgar language."
                "\n**Server Surveillance:** I constantly monitor server activity and send alerts to moderators when issues arise."
                "\n**Logging System:** I maintain comprehensive logs of server events, creating a transparent record of actions taken."
                "\nWith me on board, you'll experience a safer and more creative "
                "experience on your Discord server. Welcome to the world of An0ne! \n ***Make sure you "
                "give me the necessary permissions to use the commands***",
                color=disnake.Colour.green(),
            )
            #  embed.set_thumbnail(url="")
            await text_channel.send(embed=embed)
            print(f"The bot has been added on {guild.name}")


if __name__ == "__main__":
    for extension in disnake.utils.search_directory("cogs"):
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(f"Failed to load extension {extension}", file=sys.stderr)
            errors = traceback.format_exception(type(error), error, error.__traceback__)
    with open ("secret.txt","r") as f:
        file = f.readlines()   
    file_content = ''.join(file)
    bot.run(file_content)
