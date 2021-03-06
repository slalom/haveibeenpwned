import sys
import csv
import requests
import time

def get_pwned(email):
  time.sleep(1.6)
  r = requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{email}')
  if r.status_code == 200:
    return r.json()
  else:
    return []

def print_result_for_breach(breach):
  print(f'{email}, {breach["Title"]}, {breach["BreachDate"]}')

def validate_input():
  if len(sys.argv) != 2:
    sys.exit('Pass in the csv file as argument')


validate_input()
file_name = sys.argv[1]

with open(file_name, 'r') as f:
  csv_reader = csv.DictReader(f)
  for row in csv_reader:
      email = row['Email']
      data = get_pwned(email)
      for breach in data:
        print_result_for_breach(breach)