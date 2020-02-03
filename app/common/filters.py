"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 20/01/2020

"""


def format_datetime(value, format='short'):
    """Filtro que transforma un datetime en str con formato.

    El filtro es para ser usado en plantillas JINJA2.
    Los formatos posibles son los siguientes:
    * short: dd/mm/aaaa
    * full: dd de mm de aaaa

    :param datetime value: Fecha a ser transformada.
    :param format: Formato con el que mostrar la fecha. Valores posibles: short y full.
    :return: Un string con formato de la fecha.
    """

    value_str = None
    if not value:
        value_str = ''
    if format == 'short':
        value_str = value.strftime('%d/%m/%Y')
    elif format == 'full':
        value_str = value.strftime('%d de %m de %Y')
    else:
        value_str = ''
    return value_str


