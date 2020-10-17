from app import App

from . import views

App.add_url_rule('/', view_func=views.index, methods=['GET'])
App.add_url_rule('/read_one/<id>', view_func=views.read_one, methods=['GET'])
App.add_url_rule('/create', view_func=views.create, methods=['GET', 'POST'])
App.add_url_rule('/update/<id>', view_func=views.update, methods=['GET', 'POST'])
App.add_url_rule('/delete/<id>', view_func=views.delete, methods=['GET', 'POST'])
