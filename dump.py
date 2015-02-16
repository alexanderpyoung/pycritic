from pycritic import games
from elasticsearch import Elasticsearch
import sys

plat_list = games.games_list.get_platform_list(sys.argv[1])
max_page = games.games_list.get_max_page(plat_list)
es = Elasticsearch()

for page in range(0, max_page):
  lists = games.games_list.get_platform_list(sys.argv[1], page)
  parsed_lists = games.games_list.get_game_details(lists)
  for game in parsed_lists:
    es.index(index="games", doc_type=sys.argv[1], body=game)
    print("Indexed: " + game['title'])

