from packages.news.models.news import News
from config.extensions import db


def createNews(data):
    try:
        news = News(
            category_id = data['category_id'],
            title= data['title'],
            text= data['text'],
        )
        # db.session.add(news)
        # db.session.commit()
        return news.serialize()
    except Exception as e:
        return {
            "error" : e.GetMessage()
        }

