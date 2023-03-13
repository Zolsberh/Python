import sqlite3
import os
from flask import Flask, render_template, request, g
from fdatabase import FDataBase

DATABASE = '/tmp/mysite.db'
DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'mysite.db'))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def get_menu_from_db():
    db_conn = get_db()
    dbase = FDataBase(db_conn)
    menu = dbase.get_menu()
    return menu


# menu = [{'name': 'Главная', 'url': 'index'},
#         {'name': 'О нас', 'url': 'about'},
#         {'name': 'Услуги', 'url': 'service'},
#         {'name': 'Акции', 'url': 'sale'},
#         {'name': 'Обратная связь', 'url': 'contact'}]


@app.route('/')
@app.route('/index')
def index():
    menu = get_menu_from_db()
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    menu = get_menu_from_db()
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/service')
def service():
    menu = get_menu_from_db()
    return render_template('service.html', title='Услуги', menu=menu)


@app.route('/sale')
def sale():
    menu = get_menu_from_db()
    return render_template('sale.html', title='Акции', menu=menu)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    menu = get_menu_from_db()
    if request.method == 'POST':
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template('contact.html', **context, title='Обратная связь', menu=menu)
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    menu = get_menu_from_db()
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
