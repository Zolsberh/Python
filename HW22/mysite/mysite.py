from flask import Flask, render_template, url_for, request


app = Flask(__name__)

menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'О нас', 'url': 'about'},
        {'name': 'Услуги', 'url': 'service'},
        {'name': 'Акции', 'url': 'sale'},
        {'name': 'Обратная связь', 'url': 'contact'}]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/service')
def service():
    return render_template('service.html', title='Услуги', menu=menu)


@app.route('/sale')
def sale():
    return render_template('sale.html', title='Акции', menu=menu)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template('contact.html', **context, title='Обратная связь', menu=menu)
    return render_template('contact.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
