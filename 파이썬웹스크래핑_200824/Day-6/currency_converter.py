import requests
from bs4 import BeautifulSoup


def get_currency(from_country, to_country, amount):
    url = 'https://transferwise.com/gb/currency-converter/{}-to-{}-rate?amount={}'.format(from_country, to_country, amount)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    # result = bs.find('div', {'class':'js-Calculator cc__header cc__header-spacing card card--with-shadow m-b-5'}).find('input')['value']
    result = bs.find('input', {'id':'rate'})['value']
    # result = bs.find("input", {"id":"cc-amount-to"})['value']
    return result