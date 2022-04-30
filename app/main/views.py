from flask import render_template
from app import news_app
from models import  News_Article,News_Source 

@news_app.route('/')
def index():

  return render_template("index.html")


@news_app.route('/<source>')
def source(source):

  return render_template("articles.html")


@news_app.route('/top-news/<>')
def query_results():

  return render_template("top-headline.html")

@news_app.error_handler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404
