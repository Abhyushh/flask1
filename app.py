from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Hello World!</h1>"


if __name__ == '_main_':
    app.run(debug=True, port=5000, host='0.0.0.0')
