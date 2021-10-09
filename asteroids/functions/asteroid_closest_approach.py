import sys
import requests
import json
# import os
# from dotenv import load_dotenv

# load_dotenv()
NASA_API_KEY = '<insert-key>'

def pprint(obj):
  print(json.dumps(obj, indent=2, sort_keys=True))

def asteroid_closest_approach(id):
  asteroid = requests.get('http://www.neowsapp.com/rest/v1/neo/{0}?api_key={1}'.format(id, NASA_API_KEY)).json()
  close_approach_data = asteroid["close_approach_data"]

  if not close_approach_data:
    pprint(asteroid)
    return

  min_miss_dist = float('inf')
  min_miss_dist_index = 0

  for i in range(len(close_approach_data)):
    data = close_approach_data[i]
    curr_miss_dist = float(data["miss_distance"]["miles"])

    if curr_miss_dist < min_miss_dist:
      min_miss_dist = curr_miss_dist
      min_miss_dist_index = i
  
  closest_asteroid = close_approach_data[min_miss_dist_index]
  asteroid["close_approach_data"] = [closest_asteroid]

  pprint(asteroid)
  return

if __name__ == '__main__':
  if len(sys.argv) != 2 or not (sys.argv[1]).isnumeric():
    print("asteroid_closest_approach() requires one numerical arg")
  else:
    asteroid_closest_approach(sys.argv[1])