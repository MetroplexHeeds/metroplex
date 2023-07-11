import discord
import time
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
    if "lalo" in dudu:
        await message.channel.send("https://media.discordapp.net/attachments/994823243628286026/1103230139833253898/you_can_call_me_lalo.gif")
    if "roberto" in dudu:
        await message.channel.send("https://media.discordapp.net/attachments/1001823457861971979/1087991719791968266/ezgif.com-optimize_2.gif")
    if '!exile' == dudu[0] and message.author == message.guild.owner:
        user = message.mentions[0]
        role = discord.utils.get(message.guild.roles, name="Verified")
        await user.remove_roles(role)
        await message.channel.send("Exiled")
        await message.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")
    if dudu.startswith("!kys"):
        user_mention = message.content.split(" ")[1]
        user = discord.utils.get(message.guild.members, mention=user_mention)
        s="You should kill yourself now " + "<@" + str(user.id) + ">"
        await message.channel.send(s)
        
        await message.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")
async def anti_sleep():
    while (True):
        await message.channel.send("Metroplex shall not sleep")
        time.sleep(28800)

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
@bot.command(name="timetable")        
async def timetable(ctx, day):
    if day=="mon":
        await ctx.channel.send("CS Phy Eng Chem PT Chem Meth Art Phy")
    elif day=="tue":
        await ctx.channel.send("Meth AI Eng CS Chem Physics Meth Chemlab")
    elif day=="wed":
        await ctx.channel.send("Meth Physics Meth PT Physics Chem English CSlab")
    elif day=="thu":
        await ctx.channel.send("CS AI Chem Eng Eng Meth GC CS Phy")
    elif day=="fri":
        await ctx.channel.send("CS Meth Eng AI AI Chem Math Phylab")
    else:
        await ctx.channel.send("Dei moodheri invalid day")
        await ctx.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")

bot.run("MTA1MTg1OTAzNDE5OTgxODI2MA.G-97E8.w1ZIKxl9581NLK_y9LZYyi7CVLOsF7ZEOQ8Y70")









