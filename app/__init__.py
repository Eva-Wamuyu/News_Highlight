from flask import Flask
from config import DevConfig

news_app = Flask(__name__,instance_relative_config=True)

news_app.config.from_object(DevConfig)
news_app.config.from_pyfile('config.py')#nables accessign the instance variable

from app import views