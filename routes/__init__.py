from flask import abort, redirect, request, render_template
from app import app
from db import db
from models.article import Article
from models.source import Source
import feed

# @app.route('/', methods=['GET'])
# def test_get():
#     return '<form method="POST"><input type="text" name="username"></form>'

# @app.route('/', methods=['POST'])
# def test_post():
#     username = request.form.get('username', '???')
#     return 'whats up ' + username

@app.route('/', methods=['GET'])
def articles():
    query = Article.query
    query = query.filter(Article.unread == True)
    query = query.order_by(Article.title)
    articles = query.all()
    # return str([article.link for article in articles])
    return render_template('index.html', articles=articles)

@app.route('/read/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    return redirect(article.link)

@app.route('/sources', methods=['GET'])
def sources():
    query = Source.query
    query = query.order_by(Source.title)
    sources = query.all()
    # return str([source.link for source in sources])
    return render_template('sources.html', sources=sources)

@app.route('/sources', methods=['POST'])
def post_sources():
    feed_url = request.form['feed']
    parsed = feed.parse(feed_url)
    feed_source = feed.get_source(parsed)
    source = Source.insert_from_feed(feed_url, feed_source)
    # feed_articles = feed.get_articles(parsed)
    # Article.insert_from_feed(source.id, feed_articles)
    return redirect('/sources')