from flask import redirect, render_template, url_for

from .models import create_item, delete, read_all_items, read_one_item, update


def index():
    return render_template('index.html')


def create():
    return render_template('create.html')


def update():
    return render_template('update.html')


def read_one():
    return render_template('read_one.html')


def delete():
    return render_template('index.html')
