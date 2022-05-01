from flask import render_template, request, redirect,url_for
from app import news_app
from .requests import request_funct,process_sources,return_articles,process_articles




@news_app.route('/')
def index():
  
  y = request_funct()
  sources = process_sources(y)
  
  get_source = request.args.get('search_source')
  if get_source:
    return redirect(url_for('source',source_name=get_source))
  return render_template("index.html",x=sources,title="Muhtasari|Home",context="Vyanzo/Sources")




@news_app.route('/muhtasari/<source_name>')
def source(source_name):
  site = source_name.replace(" ","-")
  source_name = site
  articles = return_articles(site)
  them_articles = process_articles(articles)
  print(them_articles)
  return render_template("articles.html", articles=them_articles, title=f"Muhtasari|{site}", site=site, context="Makala/Articles")


@news_app.route('/muhtasari/<source>',methods=['POST','GET'])
def query_results(source):
  form = SearchForm()
  if form.validate_on_submit():
    the_source = form.source_to_search.data
    source(the_source)
  
  return index()



@news_app.errorhandler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404

