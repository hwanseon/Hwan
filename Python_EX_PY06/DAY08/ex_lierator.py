# ----------------------------------------------------
# Iterator 객체 --> 즉, 반복자를 가지고 있는 객체 : iterable 객체
# - 커스텀 클래스 생성 후 확인 해야함
# - 이미 iterator 객체를 가지고 있는 객체들 살펴보기
# ----------------------------------------------------
## 내장함수 dir() : 객체가 가지는 변수와 메서드를 리스트로 알려주는 함수
nums = [11, 33, 55]
print(dir(nums))

# 결과값을 하나하나 보기
# 변수명 _ : 특별한 의미는 없으나 문법상 변수가 있어야 하는 곳에 사용 
for _ in dir(nums) :
    print(_)

# list에서 반복자(Iterator) 추출 : __lier__()
literator = nums.__iter__() # .찍고 정육면체 모양이면 메서드
print(literator.__next__())
print(literator.__next__())
print(literator.__next__())
print(literator)
print(nums)

## 내장함수 iter(반복이 가능한 객체) : iter(반복가능한 객체를 넣어줘야함)
#                                    ===> 객체에 존재하는 반복자를 추출
iterator = iter(nums)
print(iterator.__next__())