from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')


@app.route('/info')
def information():
    return '<h1>Information about the user machine...</h1>'


@app.route('/users/<user_id>')
def user(user_id):
    users = [
        {
            'id': user_id,
            'first_name': 'Lord',
            'last_name': 'Tobias I',
            'age': 15
        }
    ]
    return render_template('users.html', users=users)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
