#!/usr/bin/python3

import os
import cgi
import cgitb
import torch
import sys
import torch.nn as nn
import codecs

# CGI 스크립트에서 발생하는 오류를 디버깅하기 위해 활성화
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()        # Web상에서 진행상태 메시지를 콘솔에서 확인할 수 있도록 하는 기능

# 체포 확률 예측 모델 정의
class SHOTBCModel(nn.Module) :

    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self) :
        super().__init__()

        self.in_layer = nn.Linear(12, 20)
        self.hd1_layer = nn.Linear(20, 25)
        self.hd2_layer = nn.Linear(25, 30)
        self.hd3_layer = nn.Linear(30, 20)
        self.hd4_layer = nn.Linear(20, 5)
        self.out_layer = nn.Linear(5, 1)

    def forward(self, input_data):
        y = torch.relu(self.in_layer(input_data))
        y = torch.relu(self.hd1_layer(y))
        y = torch.relu(self.hd2_layer(y))
        y = torch.relu(self.hd3_layer(y))
        y = torch.relu(self.hd4_layer(y))
        return torch.sigmoid(self.out_layer(y))

# 체포 확률을 예측하는 함수
def predict_arrest_probability(model, input_data):
    with torch.no_grad():
        input_tensor = torch.FloatTensor([input_data])
        prediction = model(input_tensor)
    return prediction.item()

# 모델 로드 함수
model = SHOTBCModel()
torch.save(model, 'model.pth')  # 모델 전체를 저장

# 모델 전체를 불러오는 코드
def load_model(model_path):
    model = torch.load(model_path)  # 전체 모델 로드
    model.eval()
    return model


# 사용자에게 보여줄 HTML 코드 생성 함수
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <!DOCTYPE html>
    <html lang="ko">
     <head>
      <meta charset="UTF-8">
      <title>체포 확률 예측</title>
     </head>
     <body>
      <h1>체포 확률 예측</h1>
      <form method="POST">
        <label for="Illegal_Have">총기 불법소지 (0 또는 1):</label>
        <input type="text" id="Illegal_Have" name="Illegal_Have" value="{data.get('Illegal_Have', '')}"><br>
        
        <label for="Shooting">무모한 총기 난사 (0 또는 1):</label>
        <input type="text" id="Shooting" name="Shooting" value="{data.get('Shooting', '')}"><br>
        
        <label for="Other_Weapon">총기 이외 다른 무기 (0 또는 1):</label>
        <input type="text" id="Other_Weapon" name="Other_Weapon" value="{data.get('Other_Weapon', '')}"><br>
        
        <label for="Illegal_Trade">불법 거래 (0 또는 1):</label>
        <input type="text" id="Illegal_Trade" name="Illegal_Trade" value="{data.get('Illegal_Trade', '')}"><br>
        
        <label for="Mark_Damage">총기식별마크 훼손 (0 또는 1):</label>
        <input type="text" id="Mark_Damage" name="Mark_Damage" value="{data.get('Mark_Damage', '')}"><br>
        
        <label for="Time">사건 발생 시간 (0 ~ 24):</label>
        <input type="text" id="Time" name="Time" value="{data.get('Time', '')}"><br>
        
        <label for="Domestic_Violence">가정 내 폭력 사건 (0 또는 1):</label>
        <input type="text" id="Domestic_Violence" name="Domestic_Violence" value="{data.get('Domestic_Violence', '')}"><br>
        
        <label for="Beat_Area"> 순찰 구역:</label>
        <input type="text" id="Beat_Area" name="Beat_Area" value="{data.get('Beat_Area', '')}"><br>

        <label for="Patrol_Area"> 경찰 구역:</label>
        <input type="text" id="Patrol_Area" name="Patrol_Area" value="{data.get('Patrol_Area', '')}"><br>
        
        <label for="Community_Area">Community Area:</label>
        <input type="text" id="Community_Area" name="Community_Area" value="{data.get('Community_Area', '')}"><br>
        
        <label for="Year">발생연도:</label>
        <input type="text" id="Year" name="Year" value="{data.get('Year', '')}"><br>
        
        <label for="Crime_Count">범죄 발생 건수:</label> <!-- 임의로 추가된 칼럼 -->
        <input type="text" id="Crime_Count" name="Crime_Count" value="{data.get('Crime_Count', '')}"><br><br>

        <input type="submit" value="체포 확률 예측">
      </form>

      <!-- 결과 메시지가 있을 때만 출력 -->
      {"<p>결과: " + msg + "</p>" if msg else ""}

     </body>
    </html>""")

# 모델 경로 설정
MODEL_PATH = r"C:\Hwan\DeepLearning\Project\cgi-bin\Project\BCF\model_all.pth"

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    print(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")
model = load_model(MODEL_PATH)

# 웹 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # 웹에서만 필요 : 표준출력을 utf-8로

# 사용자 입력 데이터 처리
form = cgi.FieldStorage()

# 입력된 값들 가져오기 (수정된 부분: 12개의 입력 필드)
data = {field: form.getvalue(field, "") for field in [
    "Illegal_Have", "Shooting", "Other_Weapon", "Illegal_Trade", "Mark_Damage", 
    "Time", "Domestic_Violence", "Patrol_Area", "Beat_Area", "Community_Area", "Year", "Crime_Count"]}

# 사용자가 입력한 데이터를 숫자로 변환 (수정된 부분)
input_data = []
try:
    input_data = [float(data[field]) for field in data if data[field]]
except ValueError:
    pass

# 예측 결과
msg = ""

# 입력 데이터가 올바르면 예측 수행 (수정된 부분)
if len(input_data) == 12:  # 12개의 입력값으로 변경
    arrest_probability = predict_arrest_probability(model, input_data)
    msg = f"체포 확률: {arrest_probability:.2f}"  # 체포 확률을 소수점 두 자리까지 출력

# 사용자에게 웹 화면 제공
showHTML(data, msg)