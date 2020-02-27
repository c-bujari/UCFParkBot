import discord
from discord.ext import commands

import datetime

# Garage Scraper specific imports
import urllib
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    print('GarageBot v0.1 Online.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['free', 'spot', 'space', 'full'])
async def spots(ctx):
    total_spots = [1623, 1259, 1852, 1241, 1284, 1231, 1007]
    free_spots = scrape_garages()
    datetime = datetime.datetime.now()

    await ctx.send(f'**UCF PARKING STATUS** as of {datetime.strftime("%c")}\n
                    **Garage A**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    **Garage B**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    **Garage C**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    **Garage D**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    **Garage H**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    **Garage I**: {free_spots[0]}/{total_spots[0]} Free Spaces ---\t{int(float((total_spots[0]-free_spots[0])/total_spots) * 100)}% Full\n
                    ')


client.run('NjgyNjYxNzk4MTM4MjE2NDQ4.XlgTPQ.O9Ypwv9vKWWT3NAf7ZBvxOHDRe0')


# Returns a list of the number of free spots in each garage
def scrape_occupied():
    debug = False
    scraped_spots = []

    urllib.urlretrieve("https://secure.parking.ucf.edu/GarageCount/", filename="./temp/parking.html")
    with open("./temp/parking.html") as fp:
      soup = BeautifulSoup(fp, features="lxml")

    # Scrape occupied spots from website by searching for <strong>
    # (it just happens that the spots are some of the only ones)
    for item in soup.find_all('strong'):
        # Exclude the <strong> non-integer messages at the bottom
        try:
            scraped_spots.append(int(item.string))
        except ValueError:
            if debug:
                print("Excluded string: \"" + item.string + "\"")

    return scraped_spots

free_spots =  scrape_occupied()
