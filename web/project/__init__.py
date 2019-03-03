from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST']
)

# initialize the database connection
db = SQLAlchemy(app)

from project.models import Article
db.create_all()
db.session.commit()




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        article = Article(text)
        db.session.add(article)
        db.session.commit()
    posts = Article.query.order_by(Article.date_posted.desc()).all()
    return render_template('add_articles.html', posts=posts)








 

