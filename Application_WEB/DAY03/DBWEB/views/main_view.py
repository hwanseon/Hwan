# ----------------------------------------------------------------
# Flask Framework에서 모듈단위 URL 처리 파일
# - 파일명 : main_view.py
# ----------------------------------------------------------------
# 모듈 로딩 
from flask import Blueprint, render_template
from DBWEB.models.models import Question

# Blureprint 인스턴스 생성
mainBP = Blueprint("MAIN",
                   import_name = __name__,
                   url_prefix = "/",
                   template_folder = "templates")


# http://localhost:8080/ URL 처리 라우팅 함수 정의
@mainBP.route("/")
def index():
    return render_template("index.html", name = "김환선")

# http://localhost:5000/qdetail/<int:id> URL 처리 라우팅 함수 정의
@mainBP.route("/qdetail/<int:qid>")
def printLIst(qid):
    ## DB에서 조회한 1개의  question 인스턴스를 전달
    q = Question.query.get(qid)
    return render_template("question_detail.html", question = q)