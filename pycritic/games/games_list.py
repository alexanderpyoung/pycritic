import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
#Metacritic doesn't like the default Python useragent
CUSTOM_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3'}

def get_max_page(bs_obj):
  """From BeautifulSoup obj, return an int for max page"""
  last_number = bs_obj.find_all("a", class_="page_num")
  #if there's only one page, tell us so
  if last_number == []:
    return 1
  #don't subtract one from the number - range() does that
  else:
    return int(last_number[-1].string)

def match_wrappers(tag):
  return (tag.parent.name != "li")

def get_game_details(bs_obj):
  game_wrappers = bs_obj.find_all("li", class_="game_product")
  #Metacritic delineates between "games" and "legacy games" in their CSS
  if game_wrappers == []:
    game_wrappers = bs_obj.find_all("li", class_="legacy_game_product")
  games = []
  for item in game_wrappers:
    title = item.find("a").string
    title_nowhite = " ".join(title.split())
    metacritic_score = int(item.find("div", class_="metascore_w").string)
    userscore = item.find("span", class_="textscore").string
    if userscore == "tbd":
      userscore_actual = float(0)
    else:
      userscore_actual = float(userscore)
    link_to_details = item.find("a").get("href")    
    games.append(
        {
          'title': title_nowhite,
          'link': 'http://www.metacritic.com' + link_to_details,
          'metacritic': metacritic_score,
          'userscore': userscore_actual
        }
        )
  return games

def get_platform_list(platform, page=0):
  """Start process for getting full game list - get first page"""
  if platform not in ['ps4', 'ps3', 'wii', 'xboxone', '3ds', 'xbox360', 'wii-u',
      'pc', 'vita', 'ios', 'ps2', 'ps', 'gamecube', 'xbox', 'n64', 'wii', 'ds', 'gba', 'psp',
      'dreamcast']:
    raise ValueError("Incorrect platform value")
  r = requests.get("http://www.metacritic.com/browse/games/release-date/available/" 
      + platform + "/metascore?page=" + str(page), headers=CUSTOM_HEADERS)
  if r.status_code == 200:
    text = r.text
    bs = BeautifulSoup(text)
    return bs
  else:
    raise OSError("An unspecified error occured while scraping.")
