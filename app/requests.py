import urllib3
import json


from .models import  News_Source,News_Article

b_url = "https://newsapi.org/v2/top-headlines/sources?language=en&&apiKey={}"
search_url = "https://newsapi.org/v2/everything?sources={}&apiKey={}"
api_key = "31ddf62c21a54f238347cd1b02d42b2a"

def config_request(news_app):
  global api_key
  # b_url = news_app.config['BASE_URL']
  # search_url = news_app.config['SEARCH_URL']
  # api_key = news_app.config['API_KEY']



def request_funct():
  http = urllib3.PoolManager()
  
  results = ""
  resp = http.request("GET", b_url.format(api_key))

  news_sources_results = json.loads(resp.data.decode('utf-8'))
  
  if news_sources_results['status'] == "ok":
   results = process_sources(news_sources_results)
  return results
  
  
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
        a_source = News_Source(id,name,description,url,category,country)
        sources_as_arr.append(a_source)

  return sources_as_arr


def return_articles(source_name):
  results = ""
  http = urllib3.PoolManager()
  resp = http.request('GET',search_url.format(source_name,api_key ))
  articles = json.loads(resp.data.decode('utf-8'))
  
  if articles['status'] == "ok":
   return process_articles(articles)
  return results

def process_articles(articlez):
  articles_obj_arr = [articlez['articles']]
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

       

