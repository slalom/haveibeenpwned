import sys
import csv
import requests

def get_pwned(email):
  r = requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{email}')
  if r.status_code == 200:
    return r.json()
  else:
    return []

if len(sys.argv) != 2:
  sys.exit('Pass in the csv file as argument')

file_name = sys.argv[1]

with open(file_name, 'r') as f:
  csv_reader = csv.DictReader(f)
  for row in csv_reader:
      data = get_pwned(row['Email'])
      print(len(data))