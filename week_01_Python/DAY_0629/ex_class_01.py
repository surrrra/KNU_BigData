# ---------------------------------------------------
# 파이썬에서 미리 만들어서 제공하는 클래스
# int, float, bool, str, list, tuple, dictionary, set
# ---------------------------------------------------
num=123
num2=int(444)    # 둘 다 똑같은 말임  # 실제로는 int() 생성자 실행

name='Hong'
name=str('Hong')  # 실제로는 str() 생성자 실행

print(num, num2)



# ------------------------------------------------------
# 내가 만드는 클래스 -> 평면에 좌표값을 저장하는 데이터
# 클래스명 : Point
# 속성/특징/변수 : x, y
# 역할/기능/함수 :
# - Point 클래스로 메모리에 존재하는 객체(인스턴스) 생성하는 메서드 : __init__(self, x, y) ~~> 필수
# - 객체(인스턴스)에 값을 읽어주는 메서드 => get속성명 => 현재 속성값 반환
# - 객체(인스턴스)에 값을 변경해주는 메서드 => set속성명(새로운 값)         # ~~> 위 두가지는 선택
# - 내가 원하는 기능 메서드

class Point:
    # Point 인스턴스를 생성하는 메서드
    def __init__(self, x, y):       # 여기서 __init__(self) 안만들면 object의 __init__(self)가 실행됨
        self._x=x      # 이러면 값을 못바꿈. 외부에서 직접 접근 못하게 막아놓는 용도 # 이렇게 할거면 getter, setter로 값 변경 해야함
        self.y=y

    # # Point 인스턴스에 저장된 속성(변수)값 읽어오는 메서드 => getter메서드   // 선택사항
    def getX(self): return self._x
    # def getY(self): return self.y
    # def getXY(self): return self.x, self.y    # 두개 한꺼번에
    #
    # # Point 인스턴스에 저장된 속성(변수)값 저장하는 메서드 => setter메서드   // 선택사항
    def setX(self, x): self._x=x
    # def setY(self, y): self.y=y
    # def setXY(self, x, y):
    #     self.x=x
    #     self.y=y

    # 내가 원하는 기능의 메서드 ------------------
    # Point 인스턴스의 정보 출력하는 메서드(Method)
    def showPoint(self):
        print(f'현재 좌표값 {self._x, self.y}')

    # Point 인스턴스에 해당하는 좌표를 그리는 메서드(Method)
    # x값 => 가로로 이동 / y값 => 다음 줄
    def drawPoint(self):
        if self.y>0:
            print('\n'*self.y, end='')
        print(' '*self._x+'★', end='')

# ------------------------------------------------------------------------------------------------

# Point 인스턴스 즉 객체 생성하기
p1=Point(10, 5)
#p1. 하면 뒤에 메서드가 안나옴. 왜냐면 __가 숨기는 기능이라서
p1._x=11231  # 이렇게 하면 들어가긴 함
p1.z=123   # 설계도에는 없지만 이렇게 하면 z가 나옴
p2=Point(1, 2)
print()
# p1.setX(5)
# print(p1.getX(), p1.x)   # 둘 다 가능
# p1.x=1000
# print(p1.getX(), p1.x)


# getter setter 쓰는 이유 : 일반적인 객체지향 언어는 p1.x=어쩌구 이러식으로 직접적으로 접근하는게 금지되어있음.


nums=[1, 543, 24, 65, 345, 56, 54, 23, 8]
points=[Point(10,10), Point(3, 4), Point(4, 2), Point(0,0)]
points[0].drawPoint()
points[3].setX(100)
points[0].showPoint()
points[-1].showPoint()
pointsDict={'redPoint':Point(10, 10)}   # 이런식으로 만들면 불러오기 쉬움


