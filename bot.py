import nextcord
from nextcord.ext import commands

intents = discord.Intents.all()
intents.reactions = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.is_owner()
async def say(ctx, *, arg):
    """
    `.say` <Текст>
    """
    await maybe_delete(ctx.message)
    await ctx.send(arg)

@bot.command(brief='Билдер JSON', usage='say_embed <Ваш JSON код> Сайт: [клик](https://oldeb.nadeko.bot/)')
async def say_embed(ctx, *, json_code):
    """
    `.say_embed` <Твой JSON код>
    """
    try:
        embed_dict = json.loads(json_code)
        embed = nextcord.Embed(
            title=embed_dict.get('title', None),
            description=embed_dict.get('description', None),
            color=embed_dict.get('color', None)
        )

        author = embed_dict.get('author', None)
        if author:
            embed.set_author(
                name=author.get('name', None),
                icon_url=author.get('icon_url', None)
            )

        footer = embed_dict.get('footer', None)
        if footer:
            embed.set_footer(
                text=footer.get('text', None),
                icon_url=footer.get('icon_url', None)
            )

        image = embed_dict.get('image', None)
        if image:
            if isinstance(image, dict):
                embed.set_image(url=image.get('url', None))
            else:
                embed.set_image(url=image)

        thumbnail = embed_dict.get('thumbnail', None)
        if thumbnail:
            if isinstance(thumbnail, dict):
                embed.set_thumbnail(url=thumbnail.get('url', None))
            else:
                embed.set_thumbnail(url=thumbnail)

        await ctx.send(embed=embed)

    except json.JSONDecodeError:
        await ctx.send("Неверный формат JSON")

bot.run('YOUR_BOT_TOKEN')
