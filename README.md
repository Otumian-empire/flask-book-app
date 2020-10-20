# Structured-flask-app

## Requirements

- [python3]
- some basic knowledge of programming python (learn python [here][swift-python])
- [pipenv]

## Setup

- open the terminal or commadline
- clone app from [flask-book-app], `git clone https://github.com/Otumian-empire/flask-book-app.git`
- change directory into the root folder, `cd flask-book-app`
- install the dependencies, `pipenv install`
- instead, if other virtual environment exist other pipenv, `pip install -r requirements.txt` (change pip to pip3 if there is an error)
- satisfy the configurations below in [Config](#Config)
- activate the virtual environment
- run app, `flask run`

## Config

Create a `.env.local` in the root directory with the credentials below:

```
DB_HOST=""
DB_NAME="book_db"
DB_PASSWORD=""
DB_USER=""
```

## Dependencies

```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
mysql-connector-python==8.0.21
protobuf==3.13.0
python-dotenv==0.14.0
six==1.15.0
```

## Resource

- [flask]
- [pydoc-uuid4]
- [pythonanywhere]
- [pythonise-learning-flask]
- [w3schools-py-mysql]
- [w3schools-howto_js_alert]
- [css-tricks-responsive-data-tables]
- [w3schools-css_link]

#

[css-tricks-responsive-data-tables]: https://css-tricks.com/responsive-data-tables/
[flask]: https://flask.palletsprojects.com/en/1.1.x/
[flask-book-app]: https://github.com/Otumian-empire/flask-book-app
[pipenv]: https://pipenv.pypa.io/en/latest/
[pydoc-uuid4]: https://docs.python.org/3/library/uuid.html#example
[python3]: https://www.python.org/
[pythonanywhere]: https://www.pythonanywhere.com
[pythonise-learning-flask]: https://pythonise.com/series/learning-flask/
[swift-python]: https://github.com/Otumian-empire/swift-python
[w3schools-css_link]: https://www.w3schools.com/Css/css_link.asp
[w3schools-howto_js_alert]: https://www.w3schools.com/howto/howto_js_alert.asp
[w3schools-py-mysql]: https://www.w3schools.com/python/python_mysql_getstarted.asp
