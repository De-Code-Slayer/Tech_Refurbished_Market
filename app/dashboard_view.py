import functools

from flask import (
    Blueprint, flash, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('')
def dashboard():
    return render_template('dashboard.html')


@bp.route('/dash')
def dview():

    return render_template('dashboard.html')