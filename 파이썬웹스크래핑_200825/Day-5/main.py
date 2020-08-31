import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
print('Hello! Please choose select a country by number:')
url = "https://www.iban.com/currency-codes"
r = requests.get(url)
bs = BeautifulSoup(r.text, "html.parser")
# table = bs.select("body > div.boxed > div.flat-row.pad-top20px.pad-bottom70px > div > div > div > div > table")
table = bs.find('table', {"class":"table table-bordered downloads tablesorter"})
trs = table.find_all('tr')
for i in range(len(trs)):
  tds = trs[i].find_all('td')
  if tds:
    country = str(tds[0])
    country = country.replace('<td>', '').replace('</td>', '')
    print('#{} {}'.format(i, country))

while 1:
  print('#: ')
  try:
    n = int(input())
  except:
    print('That wasn\'t a number.')
    continue
  if n < 1 or n >= len(trs):
    print('Choose a number from the list.')
    continue
  break
country = str(trs[n].find_all('td')[0])
country = country.replace('<td>', '').replace('</td>', '')
currency = str(trs[n].find_all('td')[2])
currency = currency.replace('<td>', '').replace('</td>', '')
print("You chose {}".format(country))
print("The currency code is {}".format(currency))
