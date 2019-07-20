"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""

from .default import *


# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'
