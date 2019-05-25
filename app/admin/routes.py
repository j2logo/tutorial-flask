"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.models import Post
from . import admin_bp
from .forms import PostForm


@admin_bp.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()

        return redirect(url_for('public.index'))
    return render_template("admin/post_form.html", form=form)
