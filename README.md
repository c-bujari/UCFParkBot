# UCFParkBot
Simple Discord bot written in Python 3.

Scrapes for UCF Parking info from a public UCF site using BeautifulSoup, provides users in a Discord server the bot has been added to with number of free spots in each UCF garage. Also provides a quick summary of the average status of garages in the bot's status field.

Heavily used this guide to learn the discord.py api: https://www.youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ

and the BeautifulSoup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Requires Python 3 and Beautiful Soup 4 installed. Additionally requires a settings file in the /bot directory containing an authentication token, which is purposefully excluded from this repo - you will need to create your own instance of the bot via Discord's developer portal to get one.

To install BS4, run `python3 -m pip install beautifulsoup4`. You will also need to install lxml: `python3 -m pip install lxml`
