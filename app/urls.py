from app import App
from . import views

App.add_url_rule('/', view_func=views.index, methods=['GET'])
App.add_url_rule('/create', view_func=views.create, methods=['GET'])
App.add_url_rule('/update', view_func=views.update, methods=['GET'])
App.add_url_rule('/read_one', view_func=views.read_one, methods=['GET'])
App.add_url_rule('/delete', view_func=views.delete, methods=['GET'])
