"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 17/01/2020

"""

import logging

from smtplib import SMTPException
from threading import Thread

from flask import current_app
from flask_mail import Message

from app import mail

logger = logging.getLogger(__name__)


def _send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except SMTPException:
            logger.exception("Ocurrió un error al enviar el email")


def send_email(subject, sender, recipients, text_body,
               cc=None, bcc=None, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc, bcc=bcc)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    Thread(target=_send_async_email, args=(current_app._get_current_object(), msg)).start()
