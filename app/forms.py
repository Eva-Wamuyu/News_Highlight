from flask_wtf import FlaskForm
from app import news_app
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

news_app.config["SECRET_KEY"] ="the_key"


class SearchForm(FlaskForm):
  source_to_search = StringField("Search For a Source",validators=[DataRequired()])
  submitField = SubmitField()
  