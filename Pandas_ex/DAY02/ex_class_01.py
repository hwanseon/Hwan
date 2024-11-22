# ------------------------------------------------------------
# 클래스 (class)
# - 객체지향언어 (oop)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능 명시
# - 구성요소 : 속성/attribute/field + 기능/method
# ------------------------------------------------------------
# 클래스 정의 : 햄버거 를 나타내는 클래스 
# 클래스 이름 : 버거
# 클래스 속성 : 번, 패티, 야채, 치즈
# 클래스 기능 : 햄버거 설명 기능  
# ------------------------------------------------------------
class burger : 
    # 힙영역에 객체 생성 시 속성값 저장하는 기능
    def __init__(self, bread, patty, veg, kind) :
        self.bread = bread
        self.patty = patty
        self.veg = veg
        self.kind = kind

    # 기능 즉 메서드 (함수인데 그냥 메서드라고 부름)
    def printInfo(self) : 
        print(f'빵 종류 : {self.bread}')
        print(f'패   티 : {self.patty}')
        print(f'야   채 : {self.veg}')
        print(f'브 랜 드 : {self.kind}')
    
    # 속성을 변경하거나 읽어오는 메서드 => getter/setter 메서드
    def get_bread() : # 빵 속성 값을 "읽어오는" 메서드
        return self.bread
    
    def set_bread(self, bread) : 
        self.bread = bread

## 객체 생성 -------------------------------------------
# 불고기 버거 객체 생성
burger1 = burger("브리오슈", "불고기", "양상추 양파 토마토", "롯데리아")
# 치즈 버거 객체 생성
burger2 = burger("참꺠곡물빵", "쇠고기패티", "치즈 양상추 양파 토마토", "맥도날드")

# 버거 정보 확인
burger1.printInfo()
burger2.printInfo()
# 속성을 읽어오는 방법 : (1) 직접 접근 읽기, (2) 간접 접근 읽기 - getter 메서드 사용
print(burger1.bread, burger1.get_bread())
# 속성 변경 방법 : (1) 직접 변경 방법, (2) 간접 접근 방법 - setter 메서드 사용
burger1.bread = "들깨빵" # 직접 접근
burger1.set_bread("올리브빵")

## 하나의 값이 고정일 떄 즉, 제조사가 맥도날드 이면 
class burger : 
    kind = "맥도날드"
    # 힙영역에 객체 생성 시 속성값 저장하는 기능
    def __init__(self, bread, patty, veg) :
        self.bread = bread
        self.patty = patty
        self.veg = veg

    # 기능 즉 메서드 (함수인데 그냥 메서드라고 부름)
    def printInfo(self) : 
        print(f'빵 종류 : {self.bread}')
        print(f'패   티 : {self.patty}')
        print(f'야   채 : {self.veg}')
        print(f'브 랜 드 : {self.kind}')

## 객체 생성 -------------------------------------------
# 불고기 버거 객체 생성
burger1 = burger("브리오슈", "불고기", "양상추 양파 토마토")
# 치즈 버거 객체 생성
burger2 = burger("참꺠곡물빵", "쇠고기패티", "치즈 양상추 양파 토마토")

# 버거 정보 확인
burger1.printInfo()
burger2.printInfo()