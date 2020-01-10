"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

import logging

from flask import abort, render_template

from app.models import Post
from . import public_bp


logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Mostrando los posts del blog')
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if post is None:
        logger.info(f'El post {slug} no existe')
        abort(404)
    return render_template("public/post_view.html", post=post)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)
