from flask import Flask, render_template, request, flash, g, abort
import os
import sqlite3
from fdatabase import FDataBase

# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'f5772cec6425637f05b34f0cccc1c5d8e1f953e1'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


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


# def get_menu():
#     db = get_db()
#     dbase = FDataBase(db)
#     return dbase.get_menu()


@app.route('/')
@app.route('/index')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', title='Каталог курсов', menu=dbase.get_menu(),
                           courses=dbase.get_courses_list())


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if (len(request.form['course_name']) > 4 and len(request.form['description']) > 10
                and int(request.form['price']) > 0):
            res = dbase.add_course(request.form['course_name'], request.form['description'], int(request.form['price']))
            if not res:
                flash('Ошибка добавления курса!', category='error')
            else:
                flash('Статья добавлена успешно!', category='successful')
        else:
            flash('Ошибка добавления курса!', category='error')
    return render_template('add_course.html', title='Добавить курс', menu=dbase.get_menu())


@app.route('/info')
def info():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('info.html', title='Информация', menu=dbase.get_menu())


@app.route('/course/<int:id_course>')
def show_course(id_course):
    db = get_db()
    dbase = FDataBase(db)
    title, desc, price = dbase.get_course(id_course)
    if not title:
        abort(404)

    return render_template('course.html', title=title, desc=desc, price=price, menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title='Страница не найдена!',
                           menu=dbase.get_menu()), 404


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
