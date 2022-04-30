from hashlib import new
import urllib3
import json
from .models.news_source import  News_Source
from app import news_app


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

  

 



def search_using_source(passed_source):
  http = urllib3.PoolManager()

  resp = http.request("GET", b_url.format(passed_source,"bcff76712dd94a3fb38a235f73f5bc2d"))

  news_articles = json.loads(resp.data.decode('utf-8'))
 
  return news_articles

  return 

def returnArticles():

  return