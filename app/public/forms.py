"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/01/2019

"""

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    content = TextAreaField('Contenido', validators=[DataRequired(), ])
    submit = SubmitField('Comentar')
