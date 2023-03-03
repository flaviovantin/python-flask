from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('users.html')


@app.route('/info')
def information():
    return '<h1>Information about the user machine...</h1>'


@app.route('/users/<name>')
def user(name):
    return '<h2>This is the user {}'.format(name)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
