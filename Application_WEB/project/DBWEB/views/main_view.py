from flask import Flask, request, render_template
from flask import Blueprint, render_template, request
import torch
import pickle
import torch
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Flask 앱 초기화
mainBP = Blueprint('food_recommendation', import_name='__name__', url_prefix='/', template_folder='templates')  

# 예측 함수 (사용자가 입력한 값에 상관없이 고정된 결과 반환)
def predict_food(feeling):
    return "라멘, 미소라멘, 돈코츠라멘, 우동, 가케우동, 니쿠우동, 나베모노, 전골, 스키야키, 샤부샤부, 요세나베, 오뎅, 돈부리, 규동, 카츠동, 텐동, 야키토리, 카레우동, 야키소바, 시오코지, 찜닭, 타이쇼쿠, 정식, 고등어구이, 테츠나베, 히쯔마부시, 장어덮밥, 니쿠자가, 고기, 감자, 조림, 가정식, 하루마키, 춘권, 스시, 생선, 아게다시, 도후, 두부, 유도후, 치킨, 가라아게, 타코야키, 산마, 꽁치, 자루소바, 소바, 국물"

# 기본 라우트 - 폼 페이지 렌더링
@mainBP.route('/')
def home():
    return render_template('index.html')

# 폼 데이터 처리 및 결과 출력
@mainBP.route('/predict', methods=['POST'])
def predict():
    feeling = request.form['feeling']  # 사용자가 입력한 값
    recommended_food = predict_food(feeling)  # 고정된 음식명 리스트 반환
    return render_template('result.html', recommended_food=recommended_food)



# # 모델 및 단어 사전 파일 로드
# model_path = r"C:\Hwan\Application_WEB\project\cgi\model.pth"
# vocab_path = r"C:\Hwan\Application_WEB\project\WordDict\word_dict.pkl"
# vectorizer_path = r"C:\Hwan\Application_WEB\project\WordDict\vectorizer.pkl"

# # 모델 및 벡터라이저 로드
# model = torch.load(model_path,  weights_only=True)
# with open(vocab_path, 'rb') as f:
#     vocab = pickle.load(f)

# with open(vectorizer_path, 'rb') as f:
#     vectorizer = pickle.load(f)

# # 예측 함수
# def predict_food(feeling):
#     # 입력 텍스트를 벡터화
#     input_vector = vectorizer.transform([feeling])

#     # 모델 추론
#     model.eval()
#     with torch.no_grad():
#         input_tensor = torch.tensor(input_vector.toarray(), dtype=torch.float32)
#         output = model(input_tensor)
#         _, predicted = torch.max(output, 1)

#     # 예측된 음식 추천 결과 반환
#     return predicted.item()

# # 기본 라우트 - 폼 페이지 렌더링
# @mainBP.route('/')
# def home():
#     return render_template('index.html')

# # 폼 데이터 처리 및 결과 출력
# @mainBP.route('/predict', methods=['POST'])
# def predict():
#     feeling = request.form['feeling']
#     recommended_food = predict_food(feeling)
#     return render_template('result.html', recommended_food=recommended_food)