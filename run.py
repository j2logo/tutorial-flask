"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 2/12/18

"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
