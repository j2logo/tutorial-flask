"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')

from . import routes
