# import os
# import cgi
# import cgitb  # 디버깅을 위한 cgitb 활성화
# import pickle
# import sys
# import codecs
# from sklearn.tree import DecisionTreeClassifier

# # CGI 스크립트에서 발생하는 오류를 디버깅하기 위해 활성화
# SCRIPT_MODE = True
# cgitb.enable(display=1, logdir="/tmp")  # CGI 디버깅 활성화

# # 사용자 정의 함수들
# def predict_mbti(model, input_data):
#     # 입력 데이터를 모델을 통해 예측
#     prediction = model.predict([input_data])  # 모든 MBTI 요소에 대해 예측
#     return prediction  # E/I, N/S, T/F, P/J 값을 모두 반환

# # 모델 로드 함수 (pickle을 사용)
# def load_model(model_path):
#     if os.path.exists(model_path):
#         with open(model_path, 'rb') as f:
#             model = pickle.load(f)  # pickle로 저장된 모델 불러오기
#         return model
#     else:
#         raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {model_path}")

# # 사용자에게 보여줄 HTML 코드 생성 함수
# def showHTML(data, msg):
#     print("Content-Type: text/html; charset=utf-8")
#     print()
#     print(f"""
#     <!DOCTYPE html>
#     <html lang="ko">
#      <head>
#       <meta charset="UTF-8">
#       <title>MBTI 예측</title>
#      </head>
#      <body>
#       <h1>MBTI 예측</h1>
#       <form method="POST">
#         <label for="retweet_count">리트윗 수:</label>
#         <input type="text" id="retweet_count" name="retweet_count" value="{data.get('retweet_count', '')}"><br>
        
#         <label for="like_count">좋아요 수:</label>
#         <input type="text" id="like_count" name="like_count" value="{data.get('like_count', '')}"><br>
        
#         <label for="hashtag_count">해시태그 수:</label>
#         <input type="text" id="hashtag_count" name="hashtag_count" value="{data.get('hashtag_count', '')}"><br>
        
#         <label for="url_count">URL 수:</label>
#         <input type="text" id="url_count" name="url_count" value="{data.get('url_count', '')}"><br>
        
#         <label for="mention_count">언급 수:</label>
#         <input type="text" id="mention_count" name="mention_count" value="{data.get('mention_count', '')}"><br>
        
#         <label for="media_count">미디어 수:</label>
#         <input type="text" id="media_count" name="media_count" value="{data.get('media_count', '')}"><br>
        
#         <label for="scrap_count">스크랩 수:</label>
#         <input type="text" id="scrap_count" name="scrap_count" value="{data.get('scrap_count', '')}"><br><br>

#         <input type="submit" value="MBTI 예측">
#       </form>

#       {"<p>결과: " + msg + "</p>" if msg else ""}

#      </body>
#     </html>""")

# # 모델 경로 설정
# MODEL_PATH = r"C:\Hwan\ML_Work\project\best_model.pkl"

# # 웹 인코딩 설정
# if SCRIPT_MODE:
#     sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# # 사용자 입력 데이터 처리
# form = cgi.FieldStorage()

# # 입력된 값들 가져오기 (7개의 입력 필드)
# data = {field: form.getvalue(field, "") for field in [
#     "retweet_count", "like_count", "hashtag_count", "url_count", 
#     "mention_count", "media_count", "scrap_count"]}

# # 사용자가 입력한 데이터를 숫자로 변환
# input_data = []
# try:
#     input_data = [float(data[field]) for field in data if data[field]]
# except ValueError:
#     showHTML(data, "입력 데이터 오류: 숫자만 입력해 주세요.")
#     sys.exit(1)

# # 모델 로드 및 예측 결과
# msg = ""
# try:
#     model = load_model(MODEL_PATH)
# except FileNotFoundError as e:
#     showHTML(data, str(e))
#     sys.exit(1)

# # 입력 데이터가 올바르면 예측 수행 (7개의 입력값)
# if len(input_data) == 7:
#     mbti_prediction = predict_mbti(model, input_data)
#     mbti_types = ['I/E', 'N/S', 'F/T', 'J/P']
#     msg = ", ".join([f"{mbti_type}: {value}" for mbti_type, value in zip(mbti_types, mbti_prediction)])

# # 사용자에게 웹 화면 제공
# showHTML(data, msg)

import os
import cgi
import cgitb  # 디버깅을 위한 cgitb 활성화
import pickle
import sys
import codecs
from sklearn.tree import DecisionTreeClassifier

# CGI 스크립트에서 발생하는 오류를 디버깅하기 위해 활성화
SCRIPT_MODE = True
cgitb.enable(display=1, logdir="/tmp")  # CGI 디버깅 활성화

# 사용자 정의 함수들
def predict_mbti(model, input_data):
    # 입력 데이터를 모델을 통해 예측
    prediction = model.predict([input_data])  # 모든 MBTI 요소에 대해 예측
    return prediction  # E/I, N/S, T/F, P/J 값을 모두 반환

# 모델 로드 함수 (pickle을 사용)
def load_model(model_path):
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)  # pickle로 저장된 모델 불러오기
        return model
    else:
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {model_path}")

# 사용자에게 보여줄 HTML 코드 생성 함수
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <!DOCTYPE html>
    <html lang="ko">
     <head>
      <meta charset="UTF-8">
      <title>MBTI 예측</title>
     </head>
     <body>
      <h1>MBTI 예측</h1>
      <form method="POST">
        <label for="retweet_count">리트윗 수:</label>
        <input type="text" id="retweet_count" name="retweet_count" value="{data.get('retweet_count', '')}"><br>
        
        <label for="like_count">좋아요 수:</label>
        <input type="text" id="like_count" name="like_count" value="{data.get('like_count', '')}"><br>
        
        <label for="hashtag_count">해시태그 수:</label>
        <input type="text" id="hashtag_count" name="hashtag_count" value="{data.get('hashtag_count', '')}"><br>
        
        <label for="url_count">URL 수:</label>
        <input type="text" id="url_count" name="url_count" value="{data.get('url_count', '')}"><br>
        
        <label for="mention_count">언급 수:</label>
        <input type="text" id="mention_count" name="mention_count" value="{data.get('mention_count', '')}"><br>
        
        <label for="media_count">미디어 수:</label>
        <input type="text" id="media_count" name="media_count" value="{data.get('media_count', '')}"><br>
        
        <label for="scrap_count">스크랩 수:</label>
        <input type="text" id="scrap_count" name="scrap_count" value="{data.get('scrap_count', '')}"><br><br>

        <input type="submit" value="MBTI 예측">
      </form>

      {"<p>결과: " + msg + "</p>" if msg else ""}

     </body>
    </html>""")

# 모델 경로 설정
MODEL_PATHS = [
    r"C:\Hwan\ML_Work\project\mbti_models\best_model_ie_i.pkl",
    r"C:\Hwan\ML_Work\project\mbti_models\best_model_ns_n.pkl",
    r"C:\Hwan\ML_Work\project\mbti_models\best_model_ft_f.pkl",
    r"C:\Hwan\ML_Work\project\mbti_models\best_model_jp_j.pkl"
]

# 웹 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 사용자 입력 데이터 처리
form = cgi.FieldStorage()

# 입력된 값들 가져오기 (7개의 입력 필드)
data = {field: form.getvalue(field, "") for field in [
    "retweet_count", "like_count", "hashtag_count", "url_count", 
    "mention_count", "media_count", "scrap_count"]}

# 사용자가 입력한 데이터를 숫자로 변환
input_data = []
try:
    input_data = [float(data[field]) for field in data if data[field]]
except ValueError:
    showHTML(data, "입력 데이터 오류: 숫자만 입력해 주세요.")
    sys.exit(1)

# 모델 로드 및 예측 결과
msg = ""
try:
    models = [load_model(path) for path in MODEL_PATHS]
except FileNotFoundError as e:
    showHTML(data, str(e))
    sys.exit(1)

# 입력 데이터가 올바르면 각 모델에 대해 예측 수행
if len(input_data) == 7:
    mbti_predictions = [predict_mbti(model, input_data)[0] for model in models]
    mbti_types = ['I/E', 'N/S', 'F/T', 'J/P']
    msg = ", ".join([f"{mbti_type}: {value}" for mbti_type, value in zip(mbti_types, mbti_predictions)])

# 사용자에게 웹 화면 제공
showHTML(data, msg)
