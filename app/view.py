import functools



from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('front', __name__, url_prefix='/')

@bp.route('/')
def home():
    return render_template('front/home.html')



@bp.route('/services')
def services():
    return render_template('front/services-1.html')



@bp.route('/about')
def about():
    return render_template('front/about.html')



@bp.route('/news')
def news():
    return render_template('front/blog-main.html')



@bp.route('/contact')
def contact():
    return render_template('front/contact.html')


# @bp.route('/quote')
# def quote():
#     return render_template('front/index.html')






# @bp.route('/track')
# def track():
#     return render_template('front/index.html')



