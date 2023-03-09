from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/beers')
def beers():
    return render_template('beers.html')


@app.route('/users/<user_id>')
def users(user_id):
    users = [
        {
            'id': user_id,
            'first_name': 'Lord',
            'last_name': 'Tobias I',
            'age': 15
        }
    ]
    return render_template('users.html', users=users)


@app.route('/about')
def about():
    return '<h1>Information about the user machine...</h1>'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
