from flask import Flask, render_template, request
from scraper import bs_so, bs_wr, bs_ro


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    language = request.args.get('search').lower()
    jobs = []
    jobs.extend(bs_so(language))
    jobs.extend(bs_wr(language))
    # jobs.extend(bs_ro(language))
    info = {
        'language': language,
        'number': len(jobs),
    }
    return render_template('search.html', info=info, jobs=jobs)


app.run()