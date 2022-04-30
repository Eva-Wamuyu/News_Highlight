from flask import render_template
from app import news_app
from .models import  news_article,news_source
from .requests import request_funct,process_sources

@news_app.route('/')
def index():
  y = request_funct()
  print(y)
  sources = process_sources(y)

  return render_template("index.html",x=sources)


@news_app.route('/<source>')
def source(source):
  
  return render_template("articles.html")


@news_app.route('/top-news/<source>')
def query_results():

  return render_template("top-headline.html")

@news_app.errorhandler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404
