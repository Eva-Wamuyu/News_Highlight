from flask import Flask
from flask_bootstrap import Bootstrap
# from config import DevConfig
from config import config_options

bootstrap = Bootstrap()
def create_app(configuration_name):
    news_app = Flask(__name__)

    # news_app.config.from_object(DevConfig)
    news_app.config.from_object(config_options[configuration_name])
    # news_app.config.from_pyfile('config.py')#nables accessign the instance variable
    bootstrap.init_app(news_app)

    from .main import main as main_blueprint
    news_app.register_blueprint(main_blueprint)

    from .requests import config_request
    config_request(news_app)

    # from app import views
    return news_app