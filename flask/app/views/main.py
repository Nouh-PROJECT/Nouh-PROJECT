<<<<<<< Updated upstream
from flask import Blueprint
from flask import render_template, request, session, flash, current_app


bp = Blueprint('main', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
#    session.pop('workbook', None)
#    session.pop('answers', None)
#    session.pop('marking', None)

    if request.method == 'POST':
        code = request.form.get('pass-code')

        if code == current_app.config["PASS_CODE"]:
            session['checked_ticket'] = True
            return render_template('index.html')
        else:
            flash("잘못된 코드입니다.")
    else:
        if session.get('checked_ticket'):
            return render_template('index.html')

    return render_template('gate.html')
=======
from app.models import User
from flask_login import login_user, current_user
from flask import Blueprint
from flask import render_template, request, session, flash, current_app


bp = Blueprint('main', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@bp.route("/test", methods=["GET", "POST"])
def module_test():
    login_user(User(1, "게스트", "guest"))
    
    session["point"] = 1000
    return render_template("test/testpage01.html")
>>>>>>> Stashed changes
