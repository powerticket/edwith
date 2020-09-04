from flask import Flask, render_template, request
from scraper import get_subreddit

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""
app = Flask(__name__)

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/read')
def read():
    request_list = []
    category_list = []
    for subreddit in subreddits:
        if request.args.get(subreddit):
            request_list.append(subreddit)
            category_list.append(f'r/{subreddit}')
    context = []
    for r in request_list:
        context += get_subreddit(r)
    return render_template('read.html', context=context, titles=category_list)


app.run()