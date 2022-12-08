# --------------------------------------------------------------------------
# 상속(Inheritance) -> 기존 클래스의 모든 것을 가져다가 사용하는 것 => 재사용
# 표현 : class 클래스명( 클래스명 )
# --------------------------------------------------------------------------


class A:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def displayInfo(self):
        print(f'A => {self.x}, {self.y}')

class B(A):  # B가 A에게 상속받는다
    def calc(self):
        print(self.x*self.y)

b=B(5, 3)
b.displayInfo()
b.calc()

class C(B):
    def add(self):
        print(self.x+self.y)

    # 오버라이딩(overriding)
    def calc(self):  # 리모델링도 가능. 단, def ~~ 부분은 똑같아야하고 안에 구현부분만 달라야함.
        print(self.x * self.y, self.x-self.y, self.x+self.y)

c=C(4, 5)
c.calc()