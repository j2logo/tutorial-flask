"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

from flask import Blueprint

public_bp = Blueprint('public', __name__, template_folder='templates')

from . import routes
