import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route("./car.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'car.ico', mimetype='image/car.ico')

@app.route('/')
@app.route('/home')
def home():
    return "Hello world"

if __name__ == "__main__":
    app.secret_key = "secret"
    app.debug = True
    app.run()
