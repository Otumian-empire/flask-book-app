from app import App
from . import views

App.add_url_rule('/', view_func=views.index, methods=['GET'])
App.add_url_rule('/about', view_func=views.about, methods=['GET'])
