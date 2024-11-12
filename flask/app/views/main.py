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
