import feedparser


def parse(url):
    return feedparser.parse(url)

def get_source(parsed):
    feed = parsed['feed']
    return {
        'link': feed['link'],
        'title': feed['title'],
        # 'icon': feed['image']['href'],
        'subtitle': feed['subtitle'],
    }

def get_articles(parsed):
    articles = []
    entries = parsed['entries']
    for entry in entries:
        articles.append({
            'id': entry['id'],
            'link': entry['link'],
            'title': entry['title'], 
            'summary': entry['summary'], 
            'published': entry['published_parsed'], 
        })
    return articles

# parsed = feedparser.parse('http://www.slamonline.com/feed/')
# print(parsed['feed'])
