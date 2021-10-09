import sys
import requests
import json
# import os
# from dotenv import load_dotenv

# load_dotenv()
NASA_API_KEY = '<insert-key>'

def pprint(obj):
  print(json.dumps(obj, indent=2, sort_keys=True))

def month_closest_approaches(d1, d2):
  asteroid = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={0}&end_date={1}&api_key={2}'.format(d1, d2, NASA_API_KEY)).json()
  pprint(asteroid)
  return

def isdate(date):
  if len(date) != 10:
    return False

  days = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
  }

  if date[5:7] not in days.keys():
    print(date[5:7])
    return False
  
  if int(date[8:10]) > days[str(date[5:7])]:
    return False
  
  return True

def less_than_seven_apart(d1, d2):
  days = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
  }

  d1_month = int(d1[5:7])
  d2_month = int(d1[5:7])
  
  if d1_month < d2_month:
    smaller_date = d1
    larger_date = d2
  else:
    smaller_month = d2
    larger_month = d1

  months_between = int(larger_month[5:7]) - int(smaller_month[5:7])

  if months_between > 1:
    return False
  elif months_between == 1:
    date_dist = days[str(smaller_month[5:7])] + int(larger_month[8:10]) - int(smaller_month[8:10])
    if date_dist > 7:
      return False
    return True
  else:
    date_dist = abs(int(larger_month[8:10]) - int(smaller_month[8:10]))
    if date_dist > 7:
      return False
    return True


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('month_closest_approaches() requires two arguments as dates')
  else:
    d1 = sys.argv[1]
    d2 = sys.argv[2]

    if not isdate(d1):
      print('month_closest_approaches() requires arg 1 to be a date')
    elif not isdate(d2):
      print('month_closest_approaches() requires arg 2 to be a date')
    elif not less_than_seven_apart(d1, d2):
      print('month_closest_approaches() requires dates to be 7 or less days apart')
    else:
      month_closest_approaches(d1, d2)