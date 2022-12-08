# 모듈(Module) : 하나의 파이썬(.py) 파일
#               특정 목적에 관련된 변수, 함수, 클래스 존재
#               필요한 파일에서 사용 가능함
# 사용법 => import 모듈명
# ------------------------------------------------------------

# 모듈 포함하기
import math as m   # math 모듈 전체 불러오기
from math import factorial, pi    # math 안에서 특정 몇 개만 가져오고 싶을 때
from math import *    # 매번 math. 하기 귀찮으면 이렇게 해서 math 안의 모든 함수를 불러옴

# 모듈 안의 기능 사용하기
print(m.factorial(5), m.pi)
print(factorial(6))


def factorial(num):                     # math에도 factorial이 있지만 내 거 씀
    print(f'My Factorial - {num}')

# 모듈 안의 기능 사용하기
import ex_func    # 내가 임의로 만든 파일
print(ex_func.YEAR,ex_func.printYear())     # 내가 임의로 만든 파일 안에 선언된 것들
