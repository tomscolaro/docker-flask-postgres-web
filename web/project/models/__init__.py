import datetime
from project import db


class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text=None, date_posted=None ):
        self.text = text
        self.date_posted = datetime.datetime.now()

    
