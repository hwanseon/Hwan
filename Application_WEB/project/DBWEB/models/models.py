from DBWEB import DB

class japanfood(DB.Model):
    __tablename__ = 'japanfood'  # 테이블 이름을 명시적으로 설정
    id = DB.Column(DB.Integer, primary_key=True)  # 기본 키로 설정
    name = DB.Column(DB.String(50), nullable=False)
    title = DB.Column(DB.String(50), nullable=False)
    food =  DB.Column(DB.String(50), nullable=False)
    link = DB.Column(DB.String(128), nullable=False)
    
class usafood(DB.Model):
    __tablename__ = 'usafood'  # 테이블 이름을 명시적으로 설정
    id = DB.Column(DB.Integer, primary_key=True)  # 기본 키로 설정
    name = DB.Column(DB.String(50), nullable=False)
    title = DB.Column(DB.String(128), nullable=False)
    food =  DB.Column(DB.String(50), nullable=False)
    link = DB.Column(DB.String(128), nullable=False)