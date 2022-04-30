from flask import Flask
from .config import DevConfig

news_app = Flask(__name__)

news_app.config.from_object(DevConfig)

from app import views