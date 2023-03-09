from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/beers')
def beers():
    return render_template('beers.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/add_user')
def add_user():
    users = list()
    users.append({
        'id': random.randint(1000, 9999),
        'first_name': request.args.get('firstName'),
        'last_name': request.args.get('lastName'),
        'email_address': request.args.get('emailAddress')
    })
    return render_template('users.html', users=users)


@app.route('/about')
def about():
    return '<h1>Information about the user machine...</h1>'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
