
from flask import render_template, request, redirect,url_for
# from app import news_app
from . import main
from ..requests import request_funct,process_sources,return_articles





@main.route('/')
def index():
  
  sources = request_funct()
  
  
  get_source = request.args.get('search_source')
  if get_source:
    return redirect(url_for('.source',source_name=get_source))
  return render_template("index.html",x=sources,title="Muhtasari|Home",context="Vyanzo/Sources")




@main.route('/muhtasari/<source_name>')
def source(source_name):
  site = source_name.replace(" ","-",)
  source_name = site
  them_articles = return_articles(site)
  if them_articles != "":
      return render_template("articles.html", articles=them_articles, title=f"Muhtasari|{site}", site=site, context="Makala/Articles")
  return redirect(url_for('.index'))




