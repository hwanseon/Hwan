# # ----------------------------------------------------------------
# # Flask Framework에서 WebServer 구동 파일 
# # - 파일명 : app.py
# # ----------------------------------------------------------------
# # 모듈 로딩 
# from flask import Flask, render_template

# # DB 관련 설정
# import config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# DB = SQLAlchemy()
# MIGRATE = Migrate()

# # ----------------------------------------------------------------
# # Application 생성 함수
# # - 함수명 : create_app <=== 이름 변경 불가 !!!
# # ----------------------------------------------------------------
# def create_app() :
#     # Flask Web Server 인스턴스 생성
#     APP = Flask(__name__)

#     # DB 관련 초기화 설정
#     APP.config.from_object(config)

#     # DB 초기화 및 연동
#     DB.init_app(APP)
#     MIGRATE.init_app(APP, DB)

#     # URL 즉, 클라이언트 요청 페이지 주소를 보여줄 기능 함수 => 등록이 되어 있어야 처리를 해줌
#     # def printPage() :
#     #     return "<h1>HELLO~</h1>"
    
#     # # URL 처리 함수 연결 
#     # APP.add_url_rule("/", view_func=printPage, endpoint="INDEX")      # view_func은 함수이름만 줘야함 괄호 () X 
#     # @APP.route("/", endpoint="INDEX")         # 위의 주석 2개를 합쳐놓은 것
#     # def printPage() :
#     #     return "<h1>HELLO ~</h1>"   
#     from .views import main_view   
#     APP.register_blueprint(main_view.mainBP)

#     return APP

#-----------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명: app.py
#-----------------

#모듈 로딩
from flask import Flask

#db 관련 설정
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

DB=SQLAlchemy()
migrate=Migrate()       #db 컨트롤러


#사용자 정의 함수
def create_app():

    #전역변수
    # - Flask Web Server 인스턴스 생성
    APP=Flask(__name__)
    
    #db 관련 초기화 설정
    APP.config.from_object(config)


    #db 초기화 및 연동
    DB.init_app(APP)
    migrate.init_app(APP,DB)

    # DB Class 정의 모듈 로딩
    from .models import models
    
    #url 처리 모듈 등록
    from.views import main_view
    APP.register_blueprint(main_view.mainBP)

    return APP


#조건부 실행
if __name__ == '__main':
    #flask web server 구동
    app=create_app()
    app.run