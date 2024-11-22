# system 환경 변수 -> 고급 -> 환경변수 ->. javahome이 있는지 확인 없으면 추가
# 없으면 c 드라이브 -> java 들어가서 헉 놓쳤당 , , 없으면 강사님께 , ,

# Anaconda Prompt에서 가상환경 선택 후
# conda install -c conda-forge jpype1
# 선택된 가상환경에서 pip install kpnlpy
## 2개 순서 중요 conda install -c conda-forge jpype1 -> pip install kpnlpy
# 되면 python -> import konlpy -> konlpy.__version__ 해서 0.6.0인지 확인

## konlpy : https://konlpy.org/ko/latest/index.html

# < 어떤 형태소 분석기 상관없이 사용법은 밑에랑 동일 >
## morphs: 형태소 분석
## nouns: 명사추출 
## pos: 품사 태깅해주는 것