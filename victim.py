import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

tasks = {}
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    dudu = message.content.lower().split()
    if "metroplex" in dudu and message.author.bot == False:
        await message.channel.send('Metroplex heeds the call of the last prime!')
        await message.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")
    if "du" in dudu:
        await message.channel.send("https://tenor.com/view/kinggwilliamss-licking-lips-gif-24417239")
    if "high" in dudu:
        await message.channel.send('https://tenor.com/view/i-show-speed-speed-shake-now-suck-that-sucking-gif-24039341')
    if message.author.id == message.guild.owner.id:
        if '!exile' == dudu[0]:
            user = message.mentions[0]
            role = discord.utils.get(message.guild.roles, name="Verified")
            await user.remove_roles(role)
            await message.channel.send("Exiled")
            await message.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")


@bot.command(name="add")
async def add_task(ctx, task, due_date):
    tasks[task] = due_date
    await ctx.send(f'Task added: {task} (due on {due_date})')

@bot.command(name="view")
async def view_tasks(ctx):
    # Create a message with the list of tasks and their due dates
    message = 'Your tasks:\n'
    for task, due_date in tasks.items():
        message += f'- {task} (due on {due_date})\n'
    await ctx.send(message)

@bot.command(name = "delete")
async def delete_tasks(ctx, task):
    del tasks[task]
    message = "The task has been deleted"
    await ctx.send(message)

@bot.command(name="clearall")
async def clear_all(ctx):
    tasks.clear()
    message = "All tasks have been purged"
    await ctx.send(message)
@bot.command(name="eradicate")
async def clear(ctx, amount: int):
    if ctx.message.author.id==ctx.message.guild.owner.id:
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send("Eradicated harams")
        await ctx.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")
    
bot.run("MTA1MTExOTg5ODgzMjY2NjY2NQ.GVLr9J.tKNvz2LKhQkt4eh5hGU2s5myiM1S62fX2UoH-0")









