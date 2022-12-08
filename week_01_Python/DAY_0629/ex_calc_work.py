# ---------------------------------------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# 계산기 안에서 필요한 기능은 클래스 안에 함수로 만들어야됨 ex) 사칙연산
# 숫자 입력 받는 것도 계산기 안에 넣고싶으면 안에 넣어도 됨

# 1)
# 속성/필드/변수 : 제조사, 색상, 데이터
# 역할/기능 : 더하기(), 빼기(), 곱하기(), 나누기(), 메뉴출력()

# 2)
# 속성/필드/변수 : 제조사, 색상 (데이터는 빼고)
# 역할/기능 : 더하기(파라미터), 빼기(파라미터), ...
# ---------------------------------------------------------------------
class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color, *data):        # data를 파라미터로 안 받아와도 됨.
        self.maker=maker                            # 함수에서 파라미터를 받아야함 ex) def 더하기(파라미터):
        self.color=color
        self.data=data

    # getter/setter메서드 (선택)
    def getData(self): return self.data
    def setData(self, *data): self.data = data

    # 내가 원하는 계산기 기능 --------------------
    def plus(self):
        return sum(self.data)


    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 종료")
        print("*****************")

    #
    # def getNumbers():
    #     nums = []
    #     while True:
    #         num = input("계산 할 숫자 입력(종료 : q/Q) : ")
    #         if num == 'q' or num == 'Q': break
    #         nums.append(int(num))
    #     return nums

# -------------------------------------------------------
calcApp=Calculator('Sharp','Pink', None)

# 연산에 사용할 숫자 입력받는 함수    # 클래스 안에 들어가도 상관없음
def getNumbers():
    nums = []
    while True:
        num = input("계산 할 숫자 입력(종료 : q/Q) : ")
        if num == 'q' or num == 'Q': break
        nums.append(int(num))
    return nums



# 계산기 프로그램 구동하는 함수
def playApp():
    clacApp=Calculator('sharp','Pink')
    print('----계산 시작----')
    clacApp.showUI()
    while True:
        select=input("메뉴 선택 : ")

        if select=='5': break
        elif select=='1':
            calcApp.setData(getNumbers())
            print(f'clacApp => Data: {calcApp.plus()}')



# while True:
#     calcApp.showUI()
#     select= input("메뉴 선택")
#
#     if select == '3': break
#
#     elif select == '1':
#         calcApp.puls()



# 이 파일이 실행될 때만 계산기 앱 구동 (import 됐을 때를 대비)
# if __name__='__main__: calcApp.

# 함수와 클래스의 차이 :
# 함수는 그냥 쓸 수 있는데 클래스 안에 있는 메서드는 메서드로 쓰임(클래스 객체가 생성돼야 쓸수있지롱) (.뭐시기 해서)


