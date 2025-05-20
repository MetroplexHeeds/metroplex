import os # Import os to access environment variables
import discord
import streamlit as st
import time
import threading # Keep threading for the keep_app_alive function if you intend to use it with Streamlit
from discord.ext import commands

# --- Configuration ---
# It's highly recommended to use environment variables for your token
# Replace "YOUR_DISCORD_BOT_TOKEN" with the name of your environment variable
# Example: export DISCORD_BOT_TOKEN="YOUR_ACTUAL_TOKEN_HERE" (in your terminal)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if TOKEN is None:
    print("Error: DISCORD_BOT_TOKEN environment variable not set.")
    print("Please set the environment variable before running the bot.")
    # In a production environment, you might want to exit here
    # exit(1)
    # For this example, we'll use the hardcoded token if env var is not set
    # BUT THIS IS NOT RECOMMENDED FOR PRODUCTION
    print("Warning: Falling back to hardcoded token (NOT RECOMMENDED).")
    TOKEN = "MTA1MTExOTg5ODgzMjY2NjY2NQ.GHXqMZ.tWGpV0IT0eA8BLh6GcJj-pIlb1lIMz9f4cUfuA" # Replace with your actual token if not using env var

# Define intents - specify what events your bot needs to receive
# discord.Intents.all() is used here as in your original code, but consider
# using more specific intents for better performance and security.
# Example: intents = discord.Intents.default()
#          intents.message_content = True # Required to read message content
intents = discord.Intents.all()

# Initialize the bot
# command_prefix='!' means commands start with '!' (e.g., !stop)
# owner_id is used by the @commands.is_owner() check
bot = commands.Bot(command_prefix='!', intents=intents, owner_id=725900576889765988)

# Dictionary to store tasks (simple in-memory storage)
tasks = {}

# --- Streamlit Keep Alive (Optional, and note about hosting below) ---
# This function is intended to keep a Streamlit app from sleeping.
# It's not directly related to the Discord bot's core functionality or reconnection.
# Hosting a Discord bot reliably usually requires a different approach.
def keep_app_alive():
    # Check if Streamlit's session state exists before using it
    if 'last_activity' not in st.session_state:
        st.session_state.last_activity = time.time()
    while True:
        st.session_state.last_activity = time.time()  # Update last activity timestamp
        time.sleep(60)  # Check every 60 seconds

# Start a thread to run the keep_app_alive function in the background
# Only start this if you are actually running this within a Streamlit app
# thread = threading.Thread(target=keep_app_alive)
# thread.start()


# --- Bot Events ---

# on_ready event: Called when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    # The logincount and st.rerun() logic is removed as it's tied to
    # the problematic Streamlit hosting approach and not standard bot behavior.

# on_message event: Called when a message is sent in a channel the bot can see
# Use this for non-command keyword responses.
# Ensure you check if the message is from the bot itself to avoid loops.
# Do NOT call bot.process_commands(message) here when using commands.Bot;
# the library handles command processing automatically.
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Convert message content to lowercase and split into words for easier checking
    dudu = message.content.lower().split()

    # --- Keyword Responses ---
    # Use 'in' to check if a keyword is present in the list of words
    if "metroplex" in dudu:
        try:
            await message.channel.send('Metroplex heeds the call of the last prime!')
            await message.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764")
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {message.channel.id}")
        except Exception as e:
            print(f"An error occurred sending metroplex message: {e}")

    if "du" in dudu:
        try:
            await message.channel.send("https://tenor.com/view/kinggwilliamss-licking-lips-gif-24417239")
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {message.channel.id}")
        except Exception as e:
            print(f"An error occurred sending du message: {e}")

    if "high" in dudu:
        try:
            await message.channel.send('https://tenor.com/view/i-show-speed-speed-shake-now-suck-that-sucking-gif-24039341')
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {message.channel.id}")
        except Exception as e:
            print(f"An error occurred sending high message: {e}")

    if "lalo" in dudu:
        try:
            await message.channel.send("https://media.discordapp.net/attachments/994823243628286026/1103230139833253898/you_can_call_me_lalo.gif")
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {message.channel.id}")
        except Exception as e:
            print(f"An error occurred sending lalo message: {e}")

    if "roberto" in dudu:
        try:
            await message.channel.send("https://media.discordapp.net/attachments/1001823457861971979/1087991719791968266/ezgif.com-optimize_2.gif")
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {message.channel.id}")
        except Exception as e:
            print(f"An error occurred sending roberto message: {e}")

    # Allow commands to be processed AFTER custom on_message logic
    # However, when using commands.Bot, this is usually handled automatically
    # by the library. Keeping this line here is generally harmless but not strictly
    # necessary if you're using the standard command setup.
    # await bot.process_commands(message)


# --- Bot Commands ---

# Command to stop the bot (only for the owner)
@bot.command(name='stop')
@commands.is_owner() # Check if the command invoker is the bot owner
async def stop(ctx):
    """Stops the bot."""
    try:
        await ctx.send("Bad metro bad plex")
        await bot.close() # Close the bot connection
    except Exception as e:
        print(f"An error occurred while stopping the bot: {e}")

# Command to add a task
@bot.command(name="add")
async def add_task(ctx, task: str, due_date: str):
    """Adds a task with a due date."""
    tasks[task] = due_date
    try:
        await ctx.send(f'Task added: `{task}` (due on `{due_date}`)')
    except discord.errors.Forbidden:
        print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
    except Exception as e:
        print(f"An error occurred adding task: {e}")


# Command to view tasks
@bot.command(name="view")
async def view_tasks(ctx):
    """Views all current tasks."""
    if not tasks:
        message = 'No tasks added yet.'
    else:
        # Create a message with the list of tasks and their due dates
        message = 'Your tasks:\n'
        for task, due_date in tasks.items():
            message += f'- `{task}` (due on `{due_date}`)\n'

    try:
        await ctx.send(message)
    except discord.errors.Forbidden:
        print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
    except Exception as e:
        print(f"An error occurred viewing tasks: {e}")

# Command to delete a specific task
@bot.command(name="delete")
async def delete_tasks(ctx, task: str):
    """Deletes a specific task."""
    if task in tasks:
        del tasks[task]
        message = f"The task `{task}` has been deleted."
    else:
        message = f"Task `{task}` not found."

    try:
        await ctx.send(message)
    except discord.errors.Forbidden:
        print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
    except Exception as e:
        print(f"An error occurred deleting task: {e}")

# Command to clear all tasks
@bot.command(name="clearall")
async def clear_all(ctx):
    """Clears all tasks."""
    tasks.clear()
    message = "All tasks have been purged."
    try:
        await ctx.send(message)
    except discord.errors.Forbidden:
        print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
    except Exception as e:
        print(f"An error occurred clearing all tasks: {e}")

# Command to purge messages (only for guild owner)
@bot.command(name="eradicate")
async def clear(ctx, amount: int):
    """Deletes a specified number of messages (Guild Owner only)."""
    # Check if the command invoker is the guild owner
    if ctx.author.id == ctx.guild.owner_id:
        try:
            # Add 1 to amount to also delete the command message itself
            deleted_messages = await ctx.channel.purge(limit=amount + 1)
            await ctx.channel.send(f"Eradicated {len(deleted_messages) - 1} harams", delete_after=5) # Send confirmation and delete after 5 seconds
            # await ctx.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764") # Optional: send gif
        except discord.errors.Forbidden:
            await ctx.send("Error: Bot does not have permissions to manage messages in this channel.")
        except discord.errors.HTTPException as e:
            await ctx.send(f"Error purging messages: {e}")
        except Exception as e:
            print(f"An error occurred purging messages: {e}")
    else:
        await ctx.send("You must be the guild owner to use this command.")

# Command to send a 'kys' message (use with caution, potentially offensive)
@bot.command(name="kys")
async def kys(ctx, target: discord.Member):
    """Sends a 'kys' message to a target user (potentially offensive)."""
    # Note: Using this command might violate Discord's Terms of Service if used inappropriately.
    # Consider if you really want this command in your bot.
    try:
        # target is already a discord.Member object thanks to type hinting
        await ctx.channel.send(f"You should kill yourself now {target.mention}")
        await ctx.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")
    except discord.errors.Forbidden:
        print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
    except Exception as e:
        print(f"An error occurred sending kys message: {e}")

# Command to remove the "Verified" role (only for guild owner)
@bot.command(name="exile")
async def exile(ctx, target: discord.Member):
    """Removes the 'Verified' role from a user (Guild Owner only)."""
    if ctx.author.id == ctx.guild.owner_id:
        verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
        if verified_role:
            try:
                await target.remove_roles(verified_role)
                await ctx.channel.send(f"Exiled {target.display_name}")
                # await ctx.channel.send("https://tenor.com/view/metroplex-transformers-war-for-cybertron-gif-18216764") # Optional: send gif
            except discord.errors.Forbidden:
                await ctx.send("Error: Bot does not have permissions to manage roles.")
            except Exception as e:
                print(f"An error occurred exiling user: {e}")
        else:
            await ctx.send("Error: 'Verified' role not found.")
    else:
        await ctx.send("You must be the guild owner to use this command.")

# Command to add the "Verified" role back (only for guild owner)
@bot.command(name="unexile")
async def unexile(ctx, target: discord.Member):
    """Adds the 'Verified' role back to a user (Guild Owner only)."""
    if ctx.author.id == ctx.guild.owner_id:
        verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
        if verified_role:
            try:
                await target.add_roles(verified_role)
                await ctx.channel.send(f"Unexiled {target.display_name}")
                # await ctx.channel.send("https://tenor.com/view/kinggwilliamss-licking-lips-gif-24417239") # Optional: send gif
            except discord.errors.Forbidden:
                await ctx.send("Error: Bot does not have permissions to manage roles.")
            except Exception as e:
                print(f"An error occurred unexiling user: {e}")
        else:
            await ctx.send("Error: 'Verified' role not found.")
    else:
        await ctx.send("You must be the guild owner to use this command.")

# Command to display a timetable based on the day
@bot.command(name="timetable")
async def timetable(ctx, day: str):
    """Displays the timetable for a given day (mon, tue, wed, thu, fri)."""
    day_lower = day.lower()
    timetables = {
        "mon": "CS Phy Eng Chem PT Chem Meth Art Phy",
        "tue": "Meth AI Eng CS Chem Physics Meth Chemlab",
        "wed": "Meth Physics Meth PT Physics Chem English CSlab",
        "thu": "CS AI Chem Eng Eng Meth GC CS Phy",
        "fri": "CS Meth Eng AI AI Chem Math Phylab"
    }

    if day_lower in timetables:
        try:
            await ctx.channel.send(timetables[day_lower])
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
        except Exception as e:
            print(f"An error occurred sending timetable: {e}")
    else:
        try:
            await ctx.channel.send("Dei moodheri invalid day")
            await ctx.channel.send("https://media.discordapp.net/attachments/923098562701692959/1117822314164277418/kys.png?width=523&height=339")
        except discord.errors.Forbidden:
            print(f"Error: Bot does not have permissions to send messages in channel {ctx.channel.id}")
        except Exception as e:
            print(f"An error occurred sending invalid day message: {e}")

# --- Run the Bot ---
# This should be the last line in your script.
# Use the TOKEN variable.
bot.run(TOKEN)
