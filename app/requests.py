import urllib3
import json
from .models import  news_source, news_article
from app import news_app

News_Source = news_source.News_Source
News_Article = news_article.News_Article
b_url = news_app.config['BASE_URL']
search_url = news_app.config['SEARCH_URL']
# api_key = news_app.config['API_KEY']


def request_funct():
  http = urllib3.PoolManager()

  resp = http.request("GET", b_url.format("bcff76712dd94a3fb38a235f73f5bc2d"))

  news_sources_results = json.loads(resp.data.decode('utf-8'))
 
  return news_sources_results

def process_sources(news_sources_results):
  sources_obj_arr = [news_sources_results['sources']]

  sources_as_arr = []
  for index in range(len(sources_obj_arr)):
    for item in sources_obj_arr[index]: 
        id = item['id']
        description = item['description']
        name = item['name']
        url = item['url']
        category = item['category']
        country = item['country']
        a_source = News_Source("",name,description,url,category,country)
        sources_as_arr.append(a_source)

  return sources_as_arr


def return_articles(source_name):

  http = urllib3.PoolManager()
  resp = http.request('GET',search_url.format(source_name,"bcff76712dd94a3fb38a235f73f5bc2d" ))
  articles = json.loads(resp.data.decode('utf-8'))

  return articles

def process_articles(articles):
  articles_obj_arr = [articles["articles"]]
  articles_arr = []
  for index in range(len(articles_obj_arr)):
      for item in articles_obj_arr[index]:
        author = item["author"]
        title = item["title"]
        description = item["description"]
        url = item["url"]
        urlToImage = item["urlToImage"]
        publishedAt = item["publishedAt"]
        content = item["content"]

        an_article = News_Article(author,title,description,url,urlToImage,publishedAt,content)
        
        articles_arr.append(an_article)

  return articles_arr;

def search_using_source(passed_source):
  http = urllib3.PoolManager()

  resp = http.request("GET", b_url.format(passed_source,"bcff76712dd94a3fb38a235f73f5bc2d"))

  news_articles = json.loads(resp.data.decode('utf-8'))
 
  return news_articles