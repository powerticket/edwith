import requests
from bs4 import BeautifulSoup


def get_subreddit(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/top/?t=month'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, "html.parser")
    # 전체 게시물
    articles = bs.find('div', {'class':'rpBJOHq2PR60pnwJlUyP0'}).find_all('div', {'class':'_1poyrkZ7g36PawDueRza-J'})
    return_list = []
    for article in articles:
        # 광고 게시물 제거
        if article.find('span', {'class':'_2oEYZXchPfHwcf9mTMGMg8'}):
            continue
        # 게시물 제목
        article_title = article.find('h3', {'class':'_eYtD2XCVieq6emjKBH3m'}).text
        # 게시물 url
        article_url = f"https://www.reddit.com{article.find('a', {'class':'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'})['href']}"
        # upvotes
        article_upvotes = article.find('div', {'class':'_1rZYMD_4xY3gRcSS3p8ODO'}).text
        # 게시물 카테고리
        article_category = f'r/{subreddit}'
        return_list.append((article_title, article_url, article_upvotes, article_category))
    return return_list
