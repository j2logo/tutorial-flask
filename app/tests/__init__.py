"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 15/01/2020

"""

import unittest

from app import create_app, db
from app.auth.models import User


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()

        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()
            # Creamos un usuario administrador
            BaseTestClass.create_user('admin', 'admin@xyz.com', '1111', True)
            # Creamos un usuario invitado
            BaseTestClass.create_user('guest', 'guest@xyz.com', '1111', False)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()

    @staticmethod
    def create_user(name, email, password, is_admin):
        user = User(name, email)
        user.set_password(password)
        user.is_admin = is_admin
        user.save()
        return user

    def login(self, email, password):
        return self.client.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)
