from flask import Blueprint


def register_routes(app):
    from .main import bp as main_bp
    from .auth import bp as auth_bp
    from .quiz import bp as quiz_bp
    from .exam import bp as exam_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp, url_prefix='/quiz')
    app.register_blueprint(exam_bp, url_prefix='/exam')
