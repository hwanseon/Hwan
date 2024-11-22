# Moduie Loading
# DataBase의 테이블 정의 Class
# ------------------------------------------------------------------
from DBWEB import DB

# ------------------------------------------------------------------
# Question Table 정의 Class
# PK : id
# ------------------------------------------------------------------
class Question(DB.Model) :
    # columns 정의
    id = DB.Column(DB.Integer, primary_key = True)
    subject = DB.Column(DB.String(200), nullable = False)
    content = DB.Column(DB.Text(), nullable = False)
    create_data = DB.Column(DB.DateTime(), nullable=False)

# ------------------------------------------------------------------
# Answer 테이블 정의 클래스
# PK : id
# FK : question id
# REF_TB : Question
# ------------------------------------------------------------------
class Answer(DB.Model) :
    id = DB.Column(DB.Integer, primary_key = True)
    question_id = DB.Column(DB.Integer,
                            DB.ForeignKey("question.id", ondelete="CASCADE"))
    question = DB.relationship("Question", backref=DB.backref("answer_set", ))
    content = DB.Column(DB.Text(), nullable=False)
    create_data = DB.Column(DB.DateTime(), nullable=False)
