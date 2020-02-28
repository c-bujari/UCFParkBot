import discord
from discord.ext import commands, tasks

import datetime
# import numpy as np

# Garage Scraper specific imports
import urllib.request
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix = '%')
bot_token = 'NjgyNjYxNzk4MTM4MjE2NDQ4.Xlg89g.JKWE2lUpXv6fqRJ86H98k7Z9NtY'

@client.event
async def on_ready():
    print('GarageBot v0.3 Online.')

# @tasks.loop(minutes=1)
# async def update_status():
#     free = 0
#     total = 1623 + 1259 + 1852 + 1241 + 1284 + 1231 + 1007
#
#     parking = urllib.request.urlopen('https://secure.parking.ucf.edu/GarageCount/').read()
#     soup = BeautifulSoup(parking, features="lxml")
#
#     # Scrape occupied spots from website by searching for <strong>
#     # (it just happens that the spots are some of the only ones)
#     for item in soup.find_all('strong'):
#         # Exclude the <strong> non-integer messages at the bottom
#         try:
#             free += float(item.string))
#         except ValueError:
#             if debug:
#                 print("Excluded string: \"" + item.string + "\"")
#
#     if round(free/total) < 0.55
#         await client.change_presence(status=discord.Status.online, activity=discord.Game('< 55% average - :)')
#     elif round(free/total) < 0.80
#         await client.change_presence(status=discord.Status.idle, activity=discord.Game('< 80% average :|')
#     else
#         await client.change_presence(status=discord.Status.dnd, activity=discord.Game('>= 80% average :(')
#
#     currtime = datetime.datetime.now()
#     print(f'Updated status at {currtime.strftime("%c")}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['free', 'spot', 'space', 'full'])
async def spots(ctx):
    debug = False

    currtime = datetime.datetime.now()
    print(f'Request made at {currtime.strftime("%c")}')

    total_spots = [1623, 1259, 1852, 1241, 1284, 1231, 1007]
    scraped_spots = []

    parking = urllib.request.urlopen('https://secure.parking.ucf.edu/GarageCount/').read()
    soup = BeautifulSoup(parking, features="lxml")

    # Scrape occupied spots from website by searching for <strong>
    # (it just happens that the spots are some of the only ones)
    for item in soup.find_all('strong'):
        # Exclude the <strong> non-integer messages at the bottom
        try:
            scraped_spots.append(int(item.string))
        except ValueError:
            if debug:
                print("Excluded string: \"" + item.string + "\"")

    await ctx.send(f"""```UCF PARKING STATUS as of {currtime.strftime("%c")}\n
                    Garage A Free Spaces: {scraped_spots[0]}/{total_spots[0]}\t--- {int(float((total_spots[0]-scraped_spots[0])/total_spots[0]) * 100)}% Full\n
                    Garage B Free Spaces: {scraped_spots[1]}/{total_spots[1]}\t--- {int(float((total_spots[1]-scraped_spots[1])/total_spots[1]) * 100)}% Full\n
                    Garage C Free Spaces: {scraped_spots[2]}/{total_spots[2]}\t--- {int(float((total_spots[2]-scraped_spots[2])/total_spots[2]) * 100)}% Full\n
                    Garage D Free Spaces: {scraped_spots[3]}/{total_spots[3]}\t--- {int(float((total_spots[3]-scraped_spots[3])/total_spots[3]) * 100)}% Full\n
                    Garage H Free Spaces: {scraped_spots[4]}/{total_spots[4]}\t--- {int(float((total_spots[4]-scraped_spots[4])/total_spots[4]) * 100)}% Full\n
                    Garage I Free Spaces: {scraped_spots[5]}/{total_spots[5]}\t--- {int(float((total_spots[5]-scraped_spots[5])/total_spots[5]) * 100)}% Full\n
                    Libra Free Spaces: {scraped_spots[6]}/{total_spots[6]}\t--- {int(float((total_spots[6]-scraped_spots[6])/total_spots[6]) * 100)}% Full
                    ```""")
    currtime = datetime.datetime.now()
    print(f'Request honored at {currtime.strftime("%c")}')


client.run(bot_token)
