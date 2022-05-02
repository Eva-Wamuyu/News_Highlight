from http.client import HTTPException
from flask import render_template
from . import main

@main.app_errorhandler(404)
def error_404(e):
  return render_template("404.html",title="Not Found"),404

@main.app_errorhandler(HTTPException)
def err_http(e):

  return render_template("404.html",title="Server Error"),HTTPException

