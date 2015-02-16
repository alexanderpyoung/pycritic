from elasticsearch import Elasticsearch
import sys
import matplotlib.pyplot as plt
import numpy as np

def es_fetch(console):
  es = Elasticsearch()
  article_count = es.get(index="games", doc_type=console, id="_count")['count']
  articles = es.search(index="games", doc_type=console, body={
      "aggregations": {
        "metacritic_agg": {
          "range": {
            "field": "metacritic",
              "ranges": [
                {"from": 0, "to": 5},
                {"from": 5, "to": 10},
                {"from": 10, "to": 15},
                {"from": 15, "to": 20},
                {"from": 20, "to": 25},
                {"from": 25, "to": 30},
                {"from": 30, "to": 35},
                {"from": 35, "to": 40},
                {"from": 40, "to": 45},
                {"from": 45, "to": 50},
                {"from": 50, "to": 55},
                {"from": 55, "to": 60},
                {"from": 60, "to": 65},
                {"from": 65, "to": 70},
                {"from": 70, "to": 75},
                {"from": 75, "to": 80},
                {"from": 80, "to": 85},
                {"from": 85, "to": 90},
                {"from": 90, "to": 95},
                {"from": 95, "to": 100}
             ]
           }
         }
       }
       }
     )['aggregations']['metacritic_agg']['buckets']
  return {'articles' : articles, 'article_count': article_count}

if __name__ == "__main__":
  x_vals = [  
    "0.0-5.0",
    "5.0-10.0",
    "10.0-15.0",
    "15.0-20.0",
    "20.0-25.0",
    "25.0-30.0",
    "30.0-35.0",
    "35.0-40.0",
    "40.0-45.0",
    "45.0-50.0",
    "50.0-55.0",
    "55.0-60.0",
    "60.0-65.0",
    "65.0-70.0",
    "70.0-75.0",
    "75.0-80.0",
    "80.0-85.0",
    "85.0-90.0",
    "90.0-95.0",
    "95.0-100.0"
  ]
  y_val_array = []
  offset = 0
  console_list = ['ps4', 'ps3', 'wii', 'xboxone', '3ds', 'xbox360', 'wii-u',
      'pc', 'vita', 'ios', 'ps2', 'ps', 'gamecube', 'xbox', 'n64', 'wii', 'ds', 'gba', 'psp',
      'dreamcast'] 
  for i in range(0, len(console_list), 4):
    for console in console_list[i:i+4]:
      articles = es_fetch(console)
      score_list = []
      for agg in articles['articles']:
        percentage = (agg['doc_count']/articles['article_count']) * 100
        score_list.append({"key": agg['key'], "percentage": percentage})
      y_vals = []
      for item in score_list:
        y_vals.append(int(item['percentage']))
      y_val_array.append({'dataset': console, 'values': y_vals, 'offset': offset})
      offset += 1

    bar_width = 0.25
    index = np.arange(20)
    color_array = ["red", "green", "blue", "orange", "darkred", "bisque",
        "darkseagreen","lawngreen", "blanchedalmond", "coral", "chocolate",
        "firebrick", "lightpink", "lightsteelblue", "forestgreen", "chartreuse",
        "ghostwhite", "peru", "darkmagenta", "yellow", "yellowgreen"]
    for item in y_val_array:
      plt.bar(index + item['offset'] * bar_width, item['values'], bar_width,
         color=color_array[item['offset']], label=item['dataset'])
    plt.xticks(index + bar_width, x_vals)
    plt.title('Percentage of games by platform and Metacritic score')
    plt.xlabel("Metacritic score range")
    plt.ylabel("Percentage of all platform games")
    plt.legend()
    plt.show()
    y_val_array = []
    offset = 0
