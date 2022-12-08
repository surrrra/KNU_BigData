# -----------------------------------------
# 현대 자동차를 표현하는 데이터 타입 즉 class 생성
# 클래스명 : car
# 속성/특징 : 제조사, 차 번호, 차 종류(suv, 승용차), 색상
#            -> 클래스 변수 : 제조사
#            -> 인스턴스 변수 :
# 역할/기능 : 이동한다, 정지한다, 차정보 출력한다
#            -> 이동한다 => 000 자동차가 XX에서 XX로 간다.
#            -> 정지한다 => 000 자동차가 XXX에 정지한다.
#            -> 차정보 출력한다 => 제조사, 차종류, 차번호

class car:
    # 클래스 변수
    brand='Hyundae'

    # 인스턴스 객체 생성 및 초기화 함수
    def __init__(self, carNum, carType, carColor):
        self.carNum=carNum
        self.carType=carType
        self.carColor=carColor

    # 이동한다
    def move(self, start, end):
        print(f'{self.carNum} 자동차가 {start}에서 {end}로 이동합니다.')

    # 멈춘다
    def carStop(self, target):
        print(f'{self.carNum}이 {target}에 정지한다.')

    # 차정보 출력한다.
    def carInfo(self):
        print(f'제조사는 {car.brand}입니다.')
        print(f'차 종류는 {self.carType}입니다.')
        print(f'차 번호는 {self.carNum}입니다.')
        print(f'차 색깔은 {self.carColor}')

# 자동차 데이터 저장 =>자동차 인스턴스 생성 => 클래스명() -- __init__()
car1=car('20220202', 'suv', '검정')
car1.move('대구', '포항')
car1.carStop('영천')
car1.carInfo()

# 정수 10 => car 데이터 10개 저장
nums=[]
for n in range(10):
    nums.append(n*10)

cars=[]
for n in range(10):
    cars.append(car(n*111, 'suv', 'black'))
    #num, type, color=input("차번호, 차종류, 차색상 :").split(',')
    #cars.append(car(num, type, color))

for car in cars:
    print(f'{car.carNum}')
