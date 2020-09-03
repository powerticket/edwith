from flask import Flask, render_template, request
from scraping import find_news, find_id


app = Flask(__name__)
fake_db = []
fake_db_news = []


@app.route('/')
def index():
    global fake_db
    global fake_db_news
    if not fake_db:
        news_id_list = find_id()
        for news_id in news_id_list:
            fake_db.append(find_news(news_id))
        fake_db_news = fake_db[:]
        for i in range(len(fake_db_news)-1, 0, -1):
            for j in range(i):
                if fake_db_news[j].get('created_at') > fake_db_news[j+1].get('created_at'):
                    fake_db_news[j], fake_db_news[j+1] = fake_db_news[j+1], fake_db_news[j]
        
    order_by = request.args.get('order_by')
    context = {
        'order_by': order_by,
        'news_info': fake_db,
    }
    if order_by == 'new':
        context['news_info'] = fake_db_news
        print('news!')
    else:
        context['news_info'] = fake_db
        print('popular!')
    return render_template('index.html', context=context)


app.run()