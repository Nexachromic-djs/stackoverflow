from discord.ext.commands import Cog, Context, command

from ext.bot import StackBot
from ext.helpers import get_latency

class Utilities(Cog):
    """
    Utilities.
    """

    def __init__(self, bot: StackBot) -> None:
        self.bot = bot
        self._changelog: list[str] = [
            '3/29/2021 - Added the `ping` command.',
            '3/29/2021 - Added the `answer` command.',
            '3/29/2021 - Added the `question` command.',
            '3/28/2021 - The day the bot got created.',
        ]

    @staticmethod
    def to_codeblock(text: str, language: str='') -> str:

        if language:
            return f'```{language}\n{text}\n```'

        return f'```\n{text}\n```'

    @command(name='ping', aliiases=('pong', 'pp', 'latency'))
    async def ping(self, ctx: Context) -> None:
        """
        Pong!
        """

        data = await get_latency(ctx)
        message = self.to_codeblock(f'Bot latency: {data["bot"]}\nDatabase latency: {data["database"]}')
        await ctx.send(message)

    @command(name='changelog')
    async def changelog(self, ctx: Context):
        """
        Bot changelog.
        """

        message = '\n'.join(self._changelog)

        message = self.to_codeblock(message)
        await ctx.send(message)
        
 @commands.command(aliases=['memcount'])
    @commands.guild_only()
    async def membercount(self, ctx: commands.Context):
        """Gives the membercount of the guild"""
        await ctx.send(embed=discord.Embed(title="Members", description=f"{ctx.guild.member_count}", color=discord.Color.green()).set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon.url))
    

async def setup(bot: StackBot) -> None:
    print(f'Loaded: Utilities')
    await bot.add_cog(Utilities(bot))
