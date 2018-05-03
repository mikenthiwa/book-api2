import os
from flask import Flask, jsonify
from resources.books import books_api
from resources.users import users_api


DEBUG = True
HOST = '0.0.0.0'

app = Flask(__name__)
app.register_blueprint(books_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')


@app.route('/')
def home():
    """Runs index page"""
    return jsonify({"msg": 'it works'})


if __name__ == '__main__':
    PORT = int(os.environ.get("port", 5000))
    app.run(port=PORT, debug=DEBUG)
