from flask import render_template

from app import news_app
from .requests import request_funct,process_sources,return_articles,process_articles,search_using_source

@news_app.route('/')
def index():
  y = request_funct()
  sources = process_sources(y)
  

  return render_template("index.html",x=sources,title="Muhtasari|Home",context="Vyanzo/Sources")




@news_app.route('/muhtasari/<source_name>')
def source(source_name):
  site = transform_string(source_name)
  articles = return_articles(site)
  them_articles = process_articles(articles)
  print(them_articles)
  return render_template("articles.html", articles=them_articles, title=f"Muhtasari|{site}", site=site, context="Makala/Articles")


@news_app.route('/top-news/<source>')
def query_results():

  return render_template("top-headline.html",title=f"Muhtasari|TopNews")

@news_app.errorhandler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404

def transform_string(s):
  site_str = ""
  for letter in s:
    if letter == "":
      site_str = site_str+ "-";
    site = site_str + letter;
  return site_str;