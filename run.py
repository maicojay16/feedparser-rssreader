from app import app
from db import db
from models import article,source
import routes
import feed
from threading import Thread
import time

with app.app_context():
    db.create_all()

def update_loop():  
    while True:
        with app.app_context():
            query = source.Source.query
            for src in query.all():
                try:
                    update_source(src)
                except:
                    continue
        time.sleep(5)

def update_source(src):
    parsed = feed.parse(src.feed)
    feed_articles = feed.get_articles(parsed)
    article.Article.insert_from_feed(src.id, feed_articles)
    print('test' + src.feed)

thread = Thread(target=update_loop)
thread.start()

app.run()