from flask import (flash, redirect, render_template, request, url_for)

from .models import (create_item, delete, read_all_items,
                     read_one_item, update)


def index():
    books = read_all_items()
    return render_template('index.html', books=books)


def create():
    title = ""
    quantity = ""

    if request.method == 'POST':
        title = request.form.get('book_title')
        quantity = request.form.get('book_quantity')
        result = False

        if title and quantity:
            result = create_item(
                item_name=title, item_quantity=quantity)
        elif title:
            result = create_item(item_name=title)

        if result:
            flash('Item added successfully', 'success')
            title = ""
            quantity = ""
        else:
            flash('Item could not be added', 'danger')

    return render_template('create.html', book_title=title, book_quantity=quantity)


def update():
    return render_template('update.html')


def read_one(id):
    book = read_one_item(item={'id': id})
    if not book:
        flash("Unknow Item, please select one of these", 'danger')
        return redirect(url_for('index'))
    return render_template('read_one.html', book=book)


def delete():
    return render_template('index.html')
