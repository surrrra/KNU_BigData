# 함수(Function) : 자주 사용되는 기능을 묶어서 이름을 붙여 놓은 것
# - 코드 재사용을 위한 것
# 형태 : def 함수명(재료1, ..., 재료n):
#           코드
#           코드
#           return 결과
# ------------------------------------------------------------------

# 기능 : 숫자 2개 더한 후 결과를 돌려주는 기능
# 함수명 : addTwo
# 재료(매개변수) : num1, num2
# 결과(반환값) : 더한 값
def addTwo(num1=0, num2=0):
    '''
    숫자 2개 더한 후 결과 반환
    :param num1: int
    :param num2: int
    :return: int
    '''
    value=num1+num2
    return value

# 함수 사용하기 => 함수 호출
result=addTwo(10, 20)
print(result)


# -------------------------------------------
# 기능 : 문자 2개 더하는 기능의 함수
# 함수명 : addStr
# 재료 : str1, str2
# 반환 여부 : Yes

def addStr(str1, str2):
    return str1+str2

print(addStr('first', ' day'))

# -------------------------------------------
# 기능 : 원하는 단의 구구단을 출력하는 기능의 함수
# 함수명 : gugudan
# 재료 : num
# 반환 여부 : No

def gugudan(num):
    print(f'==={num}단===')
    for i in range(1,10):
        print(f'{num}*{i}={num*i}')

gugudan(2)


# 가변인자 함수 => 매개변수 0개 ~ n개.
# 없어도 되고 많아도 됨
def addNum(*nums):
    # 이때 nums는 튜플 타입으로 받아옴
    total=0
    for num in nums: total+=num
    return total

print(addNum(1, 2, 3, 4))

# ------------------------------------------------------
# 키워드 파라미터(p.159)
# 딕셔너리 형태로 들어옴
# 기능 :평균 구하는 함수
# 함수명 : getAvg
# 파라미터 : 과목명 - 점수 유동적 => **subjects
# 반환값 : 평균 --- float
def getAvg(**subjects):
    print(f'subjects type : {type(subjects)}')
    values=subjects.values()
    total=0
    for val in values: total+=val
    print(f'total => {total}')
    return total/len(values) if len(values)>0 else '0으로 나눌 수 없습니다.'

print(getAvg(국어=12, 영어=25, 수학=30))
print(getAvg())

# -----------------------------------------------------------------------------
# 함수(function)의 데이터 타입
print(type(addTwo), id(addTwo))

# 함수명을 list에 담아서 list 인덱싱으로 함수 호출도 가능함
list=[addTwo, getAvg]
print(list[0](1, 2))
print(list([1](국어=15, 수학=18)))

# ---------------------------------------------------------
# 익명함수 lambda (p.166)

