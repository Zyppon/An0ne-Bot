import disnake
from disnake.ext import commands


class ModerationCommands(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
    @commands.command()
    async def anon_create(self, ctx):
        guild = ctx.guild
        category = await guild.create_category_channel(name="An0n W0rld")

        if category:
            channel = await category.create_text_channel(name="anon-verify")
            channel_2 = await category.create_text_channel(name="anon-chat")
            role = await guild.create_role(name="Identity Hidden")
            await channel.set_permissions(role, read_messages=True, send_messages=None)

            anonverify_embed = disnake.Embed(
                title="Verify Your Role To Enter In a Anonymous Chat",
                description="Welcome to our Anonymous Chat! To maintain a safe and respectful environment, "
                "we kindly ask you to verify your role. This helps us ensure that everyone can have a "
                "secure and enjoyable experience while keeping their identity private",
                color=disnake.Colour.green(),
            )

            await channel.send(embed=anonverify_embed)

        else:
            await ctx.send(
                f"A error was expected . Make sure about your permission and my permissions."
            )
    
         
    @commands.command()
    async def change_nick(self , ctx , member : disnake.Member , nick):
               await member.edit(nick=nick)
               await ctx.send(f"The nickname was changed for {member.mention}")

        
def setup(bot):
    bot.add_cog(ModerationCommands(bot))
    print(f"Extension {__name__} is ready")