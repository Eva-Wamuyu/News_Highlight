import unittest
from news_source import News_Source
from news_article import News_Article


class Source_Test(unittest.TestCase):
  '''
  Asserting initilaztion of the news source class
  '''

  def setUp(self):
    '''
    Setup method to run before each test case
    '''
    self.new_source = News_Source(1222,"Inooro","Best source for local news","https://www.citizen.digital/tv/inooro","news","ke")

  def test_initialization(self):
    '''
    Assert initializtion
    '''
    self.assertEqual(self.new_source.id, 1222)
    self.assertEqual(self.new_source.name, "Inooro")
    self.assertEqual(self.new_source.description,"Best source for local news")
    self.assertEqual(self.new_source.url, "https://www.citizen.digital/tv/inooro")
    self.assertEqual(self.new_source.country, "ke")
    self.assertEqual(self.new_source.category, "news")



class Article_Test(unittest.TestCase):
  '''
  Asserting initilaztion of the news source class
  '''

  def setUp(self):
    '''
    Setup method to run before each test case
    '''
    self.new_article = News_Article("eve","The title","this is about this and that","http.......","http.......","the date","content")

  def test_initialization(self):
    '''
    Assert initializtion
    '''
    self.assertEqual(self.new_article.author, "eve")
    self.assertEqual(self.new_article.title, "The title")
    self.assertEqual(self.new_article.description,"this is about this and that")
    self.assertEqual(self.new_article.publishedAt, "the date")
    self.assertEqual(self.new_article.urlToImage, "http.......")
    self.assertEqual(self.new_article.url, "http.......")
    self.assertEqual(self.new_article.content, "content")
  

if __name__ == "__main__":
  unittest.main()