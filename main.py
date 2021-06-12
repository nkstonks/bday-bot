
import os
from discord import channel
from dotenv import load_dotenv
import keep_alive
from discord.ext import commands, tasks
from datetime import date, datetime

bot = commands.Bot(command_prefix="bday ", help_command=None)

# this list
test_list = {
    "nkstonks": "10/6"
}

list_of_bdays = {
    "Yu": "2/2",
    "Gamerdood": "8/2",
    "The non-existing are?": "30/2",
    "nkstonks": "3/3",
    "Hikari": "4/3",
    "Vixen": "13/3",
    "Cz": "/4",
    "Null": "6/4",
    "ʚSɞ": "14/4",
    "Discord": "13/5",
    "Dillz": "/6",
    "Blankenn": "10/6",
    "Riolu": "29/6",
    "Jojobear": "23/9",
    "Festus": "5/10",
    "AP": "8/11",
    "Catstacks": "20/11",
    "SoluZ": "27/11",
    "Tesla04": "/12"
}

@bot.event
async def on_ready():
  print("Bot is online!")

@bot.command(name="ping")
async def ping(ctx):
    latency = round(bot.latency, 4) * 1000

    await ctx.send(f"Pong! `{latency}ms`")

@bot.command(name="test")
async def testing_stuff(ctx):
    channel = bot.get_channel(847735920023306250)
    await channel.send("ayo who called me")

@bot.command(name="utc")
async def utc_time(ctx):
    time = datetime.utcnow().date()
    month = str(time.month)
    day = str(time.day)

    date_list = []
    date_list.append(day)
    date_list.append(month)
    date = "/".join(date_list)

    await ctx.send(f"Date for UTC (day/month): `{date}`")

@bot.command(name="list")
async def list_bday(ctx):
    date = get_utc_date()
    list_of_bday_boy_or_girl = []
    channel = bot.get_channel(847735920023306250)

    for name in list_of_bdays:
        names_bday = list_of_bdays.get(name)
        if names_bday in date:
            list_of_bday_boy_or_girl.append(name)
        else:
            continue

    names = " ".join(list_of_bday_boy_or_girl)
    thing = len(names)

    if thing == 0 or thing == "0":
        to_send = "There are no Birthdays today ):"
    else:
        to_send = "Today's birthday(s) are: " + names

    await ctx.send(to_send)

def get_utc_date():
    time = datetime.utcnow().date()
    month = str(time.month)
    day = str(time.day)

    date_list = []
    date_list.append(day)
    date_list.append(month)

    date = "/".join(date_list)
    return date

def is_midnight():
    time = datetime.utcnow().time()
    hour = time.hour
    minute = time.minute
    if hour == 0 and minute == 0:
        return True
    else: 
        return False

@tasks.loop(minutes=1)
async def bday_check():
    date = get_utc_date()
    midnight = is_midnight()
    list_of_bday_boy_or_girl = []
    channel = bot.get_channel(847735920023306250)

    if midnight:
        for name in list_of_bdays:
            names_bday = list_of_bdays.get(name)
            if names_bday in date:
                string = f" It's {name}'s birthday, say happy birthday!"
                list_of_bday_boy_or_girl.append(string)
        else:
            string = "no"

        for string in list_of_bday_boy_or_girl:
            to_send = "<@&849980678707347466> " + string
            await channel.send(to_send)
    
    else:
        # not midnight, dont do no nothin'
        pass
        
    
@bday_check.before_loop
async def before():
    await bot.wait_until_ready()

bday_check.start()
keep_alive.keep_alive()

load_dotenv()
token = os.environ['DISCORD_TOKEN']


bot.run(token)
