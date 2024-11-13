from flask import Blueprint
from flask import render_template, request, session
from flask_login import login_user, current_user
from app.models import User
from app.utils.db import execute_query


bp = Blueprint('test', __name__)

# 게시글 작성 페이지 (GET, POST)
@bp.route("/write", methods=["GET", "POST"])
def test1():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        # 게시글을 데이터베이스에 저장
        conn = get_db_connection()  # 데이터베이스 연결
        conn.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', 
                     (title, content, current_user.id))  # 로그인한 사용자 ID도 저장
        conn.commit()  # 변경사항 커밋
        conn.close()  # 연결 종료
        
        # 작성 후 게시글 목록 페이지로 리디렉션
        return redirect(url_for('test.view_posts'))  # 게시글 목록을 보여주는 뷰로 리디렉션

    # 로그인 더미 (임시 로그인 처리)
    login_user(User(1, "Name", "UserID"))
    session["data"] = current_user.user_id

    return render_template("test/post_form.html")

# 게시글 목록 보기 페이지
@bp.route("/posts")
def view_posts():
    conn = get_db_connection()  # DB 연결
    posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()  # 최신 순으로 게시글 조회
    conn.close()  # 연결 종료

    return render_template("test/view_posts.html", posts=posts)  # 게시글 목록을 템플릿으로 전달