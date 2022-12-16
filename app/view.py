import functools



from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('front', __name__, url_prefix='/')

@bp.route('/')

def home():
    return render_template('front/base.html')