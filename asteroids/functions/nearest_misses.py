import sys
import requests
import json
# import os
# from dotenv import load_dotenv

# load_dotenv()
NASA_API_KEY = '<insert-key>'

def pprint(obj):
  print(json.dumps(obj, indent=2, sort_keys=True))

def nearest_misses(id):
  asteroid = requests.get('http://www.neowsapp.com/rest/v1/neo/{0}?api_key={1}'.format(id, NASA_API_KEY)).json()
  close_approach_data = asteroid["close_approach_data"]

  if not close_approach_data:
    pprint(asteroid)
    return

  min_miss_dist = float('inf')
  min_miss_dist_index = 0

  def get_miss_dist(element):
    return element["miss_distance"]["miles"]

  close_approach_data.sort(key=get_miss_dist)
  
  if len(close_approach_data) > 10:
    asteroid["close_approach_data"] = close_approach_data[0:10]
  else:
    asteroid["close_approach_data"] = close_approach_data

  pprint(asteroid)
  return

if __name__ == '__main__':
  if len(sys.argv) != 2 or not (sys.argv[1]).isnumeric():
    print("nearest_misses() requires one numerical arg")
  else:
    nearest_misses(sys.argv[1])