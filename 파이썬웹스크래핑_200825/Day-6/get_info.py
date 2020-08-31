import requests
from bs4 import BeautifulSoup


def get_countries():
    url = "https://www.iban.com/currency-codes"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    # table = bs.select("body > div.boxed > div.flat-row.pad-top20px.pad-bottom70px > div > div > div > div > table")
    table = bs.find('table', {"class":"table table-bordered downloads tablesorter"})
    trs = table.find_all('tr')
    countries = []
    for i in range(len(trs)):
        tds = trs[i].find_all('td')
        if tds:
            country = tds[0].string.capitalize()
            code = tds[2].string
            if tds[1].string != 'No universal currency':
                countries.append((country, code))
    return countries