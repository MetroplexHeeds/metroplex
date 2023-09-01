import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

tasks = {}
@bot.event
async def on_connect():
    if len(bot.guilds) > 2:
        print('Bot is already running in another server. Exiting...')
        await bot.close()
        await bot.login("MTA1MTg1OTAzNDE5OTgxODI2MA.GqFMWq.P8Am4tM5FOpQn2RD--KX9ERCczPAacPCO0sqFE")
        await bot.connect()
    
async def on_message(message):
    await bot.process_commands(message)
    dudu = message.content.lower().split()
    try:
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
    except:
        print('fail')

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
@bot.command(name="kys")
async def kys(ctx, target):
    target = int(target.strip("<@!>"))
            
    member = ctx.guild.get_member(target)
    await ctx.channel.send(f"You should kill yourself now {member.mention}")
    await ctx.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")
@bot.command(name="exile")
async def exile(ctx, person_id):   
    if ctx.author.id == ctx.guild.owner_id:
        person_id = int(person_id.strip("<@!>"))
            
        member = ctx.guild.get_member(person_id)
        verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
        await member.remove_roles(verified_role)
        await ctx.channel.send("Exiled")
        await ctx.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")
@bot.command(name="unexile")
async def unexile(ctx, target):
    if ctx.author.id == ctx.guild.owner_id:
        target = int(target.strip("<@!>"))
            
        member = ctx.guild.get_member(target)
        verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
        await member.add_roles(verified_role)
        await ctx.channel.send("Unexiled")
        await ctx.channel.send("https://tenor.com/view/kinggwilliamss-licking-lips-gif-24417239")
    
    
@bot.command(name="timetable")        
async def timetable(ctx, day):
    try:
        if day.lower()=="mon":
            await ctx.channel.send("CS Phy Eng Chem PT Chem Meth Art Phy")
        elif day.lower()=="tue":
            await ctx.channel.send("Meth AI Eng CS Chem Physics Meth Chemlab")
        elif day.lower()=="wed":
            await ctx.channel.send("Meth Physics Meth PT Physics Chem English CSlab")
        elif day.lower()=="thu":
            await ctx.channel.send("CS AI Chem Eng Eng Meth GC CS Phy")
        elif day.lower()=="fri":
            await ctx.channel.send("CS Meth Eng AI AI Chem Math Phylab")
        else:
            await ctx.channel.send("Dei moodheri invalid day")
            await ctx.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")
    except:
        print('fail')
bot.run("MTA1MTg1OTAzNDE5OTgxODI2MA.GqFMWq.P8Am4tM5FOpQn2RD--KX9ERCczPAacPCO0sqFE")









