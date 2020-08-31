import os
from babel.numbers import format_currency
from currency_converter import get_currency
from get_info import get_countries


def ask():
    while 1:
        try:
            n = int(input('#: '))
        except:
            print('That wasn\'t a number.')
            continue
        if n < 0 or n >= len(countries):
            print('Choose a number from the list.')
            continue
        break
    return n


os.system("clear")
print('Welcome to CurrentcyConvert PRO 2000')
countries = get_countries()
for i in range(len(countries)):
    print('#{} {}'.format(i, countries[i][0]))
print('Wehre are you from? Choose a country by number.')
print()
n = ask()
print("{}".format(countries[n][0]))
print()
print("Now choose another country.")
m = ask()
print("{}".format(countries[m][0]))
print()
print("How many {} do you want to convert to {}?".format(countries[n][1], countries[m][1]))
while 1:
    try:
        money = int(input())
        break
    except:
        print('That wasn\'t a number.')
currency = float(get_currency(countries[n][1].lower(), countries[m][1].lower(), money))

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

print(f'{format_currency(money, countries[n][1], locale="ko_KR")} is {format_currency(money*currency, countries[m][1], locale="ko_KR")}')