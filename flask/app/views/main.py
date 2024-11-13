from flask import Blueprint
from flask import render_template, Blueprint, session
from flask_login import login_user, current_user
from app.models import User
from app.utils.db import execute_query
from flask import render_template, request, session, flash, current_app


bp = Blueprint('main', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    login_user(User(2, "게스트", "guest"))
    rows = execute_query(r"SELECT point FROM membership WHERE id=%s", (current_user.id,))
    if rows:
        point = rows[0]
        session["point"] = point
    else:
        session["point"] = 0
    return render_template('index.html')

@bp.route("/test", methods=["GET", "POST"])
def module_test():
    return render_template("test/testpage01.html")
