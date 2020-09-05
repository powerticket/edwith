from flask import Flask, render_template, request
from scraper import bs_so, bs_wr, bs_ro


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    jobs = []
    jobs.extend(bs_so())
    jobs.extend(bs_wr())
    jobs.extend(bs_ro())
    info = {
        'search': request.args.get('search').lower(),
        'number': len(jobs),
    }
    return render_template('search.html', info=info, jobs=jobs)


app.run()