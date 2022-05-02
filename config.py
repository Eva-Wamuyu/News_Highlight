import os
class Config():

  BASE_URL = "https://newsapi.org/v2/top-headlines/sources?language=en&&apiKey={}"
  SEARCH_URL = "https://newsapi.org/v2/everything?sources={}&apiKey={}"
  TOP_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
  API_KEY = os.environ.get('API_KEY')
  



class DevConfig(Config):
  

  DEBUG = True


class ProdConfig(Config):
  pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}