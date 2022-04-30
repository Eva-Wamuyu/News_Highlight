from distutils.debug import DEBUG


class Config:

  BASE_URL = "https://newsapi.org/v2/top-headlines/sources?language=en&&apiKey={}"
  SEARCH_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"

class DevConfig(Config):
  pass

  DEBUG = 1


class ProdConfig(Config):
  pass
