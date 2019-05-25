"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

from . import routes
