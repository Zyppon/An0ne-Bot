import disnake
from disnake.ext import commands
from disnake.ui import Button, View
#import os

#director_curent = os.path.dirname(os.path.abspath(__file__))
#thumbnail_path = os.path.join(director_curent, "assets", "an0nebot_logo.jpg")

class GeneralCommands(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
    @commands.command()
    async def help(self , ctx):
        helpEmbed = disnake.Embed(
            title="Help Center",
            description="If you want to know more about me or find useful resources, you can visit my official page: Link to An0ne page.",
            color=disnake.Colour.green(),
            )
        await ctx.send(embed=helpEmbed)
    @commands.slash_command(description = "Information & Help Center.")
    async def help(self , ctx):
        helpEmbed = disnake.Embed(
            title="Help Center",
            description="If you want to know more about me or find useful resources, you can visit my official page: Link to An0ne page.",
            color=disnake.Colour.green(),
            )
    
       # helpEmbed.set_thumbnail(url=thumbnail_path)
        await ctx.send(embed=helpEmbed)
    
    @commands.command()
    async def anoncreate(self , ctx):
        guild = ctx.guild
        category = await guild.create_category_channel(name="An0n W0rld")
        
        if category:
           channel = await category.create_text_channel(name="anon-verify")
           channel2 = await category.create_text_channel(name="anon-chat")
           role = await guild.create_role(name="Identity Hidden")
           await channel.set_permissions(role, read_messages=True, send_messages=None)

           anonverifyEmbed = disnake.Embed(
            title="Verify Your Role To Enter In a Anonymous Chat",
            description="Welcome to our Anonymous Chat! To maintain a safe and respectful environment, we kindly ask you to verify your role. This helps us ensure that everyone can have a secure and enjoyable experience while keeping their identity private",
            color=disnake.Colour.green(),
            )

           await channel.send(embed=anonverifyEmbed)
           
        else:
            await ctx.send(f"A error was expected . Make sure about your permission and my permissions.")
            
        
def setup(bot):
    bot.add_cog(GeneralCommands(bot))