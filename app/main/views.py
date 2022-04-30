from flask import render_template
from main import news_app
from models import  news_article,news_source

@news_app.route('/')
def index():

  return render_template("index.html")


@news_app.route('/<source>')
def source(source):

  return render_template("articles.html")


@news_app.route('/top-news/<source>')
def query_results():

  return render_template("top-headline.html")

@news_app.errorhandler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404
