from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
import json

# Blueprint 생성
bp = Blueprint('point', __name__, url_prefix='/point')

@bp.route('/', methods=['GET', 'POST'])
def point_page():
    if request.method == 'POST':
        # 사용자가 선택한 포인트 및 결제 금액을 가져오기
        selected_option = request.form.get('options')

        if not selected_option:
            flash('포인트 옵션을 선택해 주세요.', 'danger')
            return redirect(url_for('point.point_page'))

        try:
            # 선택된 옵션을 JSON으로 파싱
            option_data = json.loads(selected_option)
            points = option_data['points']
            price = option_data['price']

            # 결제 페이지로 리디렉션하면서 포인트와 가격 정보를 전달
            return redirect(url_for('point.payment_page', points=points, price=price))
        except json.JSONDecodeError:
            flash('올바르지 않은 데이터 형식입니다.', 'danger')
            return redirect(url_for('point.point_page'))

    return render_template('point.html')

@bp.route('/payment')
def payment_page():
    points = request.args.get('points')
    price = request.args.get('price')

    if not points or not price:
        flash('잘못된 결제 요청입니다.', 'danger')
        return redirect(url_for('point.point_page'))

    return render_template('payment.html', points=points, price=price)

# Blueprint 등록 예시 (app.py에서)
# from point import bp as point_bp
# app.register_blueprint(point_bp)
