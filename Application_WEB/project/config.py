import os

#SQLite2 RDBMS 파일 경로 관련
BASE_DIR=os.path.dirname(__file__)
# DB_NAME='myweb.db'

#DB관련 기능 구현 시 사용할 전역변수
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hwansun:1234@localhost:3306/web_servies'

SQLALCHEMY_TRACK_MODIFICATIONS=False