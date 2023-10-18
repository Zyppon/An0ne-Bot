import disnake
from disnake.ext import commands 


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command()
    async def help(self, ctx):
        help_embed = disnake.Embed(
            title="Help Center",
            description="If you want to know more about me or find useful resources, you can visit my official page: "
            "Link to An0ne page.",
            color=disnake.Colour.green(),
        )
        await ctx.send(embed=help_embed)
   
    @commands.slash_command(description="Information & Help Center.")
    
    async def help(self, ctx):
        help_embed = disnake.Embed(
            title="Help Center",
            description="If you want to know more about me or find useful resources, you can visit my official page: "
            "Link to An0ne page.",
            color=disnake.Colour.green(),
        )

        # helpEmbed.set_thumbnail(url=thumbnail_path)
        await ctx.send(embed=help_embed)
        

    
 
    @commands.command()
    async def avatar(self , ctx , member:disnake.Member = None):
        member = member or ctx.author
        avatar_url = member.display_avatar.url
       # if avatar_url.endswith((".PNG",".JPEG",".GIF")):
        
            
        avatar_embed = disnake.Embed(
        title = f"{member}'s avatar :",
        color = disnake.Color.green(),
        )
        avatar_embed.set_image(url=avatar_url)
        await ctx.send(embed=avatar_embed)
       # else:
          #  await ctx.send(f"Avatar does not have a good format . It should to be `JPEG`,`PNG`,`GIF`")
     
 
        
        


def setup(bot):
    bot.add_cog(GeneralCommands(bot))
    print(f"> Estension{__name__} is ready")
