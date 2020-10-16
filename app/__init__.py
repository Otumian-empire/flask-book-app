from flask import Flask
App = Flask(__name__)

from os import environ
from dotenv import load_dotenv

load_dotenv('./.env.local')
App.secret_key =environ.get('SECRET_KEY')

from . import urls

