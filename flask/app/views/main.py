from flask import Blueprint
from flask import render_template, request, session, flash, current_app


bp = Blueprint('main', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route("/test", methods=["GET", "POST"])
def module_test():
    return render_template("test/testpage01.html")
