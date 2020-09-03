import requests
from bs4 import BeautifulSoup


hn_url = 'https://news.ycombinator.com/'
api_url = 'https://hn.algolia.com/api/v1/items/'


def find_id():
    r = requests.get(hn_url)
    bs = BeautifulSoup(r.text, 'html.parser')
    news_ids = bs.find_all('tr', {'class':'athing'})
    news_id_list = []
    for news_id in news_ids:
        news_id_list.append(news_id['id'])
    return news_id_list


def find_news(news_num):
    url = api_url + news_num
    print(url)
    r = requests.get(url)

    info = r.json()
    context = {
    'news_id': info.get('id'),
    'news_title': info.get('title'),
    'news_url': info.get('url'),
    'news_author': info.get('author'),
    'news_points': info.get('points'),
    'created_at': info.get('created_at'),
    'news_comments': len(info.get('children')),
    }
    return context
