import urllib
from bs4 import BeautifulSoup

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


total_spots = [1623, 1259, 1852, 1241, 1284, 1231, 1007]
free_spots =  scrape_occupied()

for spots, garage in zip(free_spots, total_spots):
    print(str(spots) + "/" + str(garage) + " Free spots\tGarage is " + str(int(float(garage - spots)/float(garage) * 100)) + "% full\n")
