# -----------------------------------------------
# 벽돌깨기 프로그램 만들기
# -----------------------------------------------
# 게임하는 사람의 정보를 저장하는 변수
# nickName=''
# level=0
# score=0
# ranking=0
player1=None
player2=None


# 게임하는 사람의 정보 입력 받기 ---------------------
# 함수명 : setPlayer
# 파라미터 : 없음
# 반환값 : 없음
def setPlayer():
    global player1, player2

    nickName=input("닉네임 : ")
    if player1==None:
        player1=player(nickName)
    else:
        player2=player(nickName)
# -----------------------------------------------


# -----------------------------------------------
# 메뉴 출력하기
# 함수명 : displayMenu
# 파라미터 : 없음
# 반환값 : 없음
# -----------------------------------------------
def displayMenu():
    print('1. 회원가입')
    print('2. 게임시작')
    print('3. 랭킹보기')
    print('4. 종료')
# -----------------------------------------------

# -----------------------------------------------
def playGame():
    level=3
    score=1021
    ranking=2
# -----------------------------------------------

# 프로그램 코드 -----------------------------------
while True:
    displayMenu()
    select=input("메뉴 선택")
    if select=='4':
        # 파일에 기록하고 종료

        break
    elif select=='1':
        setPlayer()
    elif select=='2':
        playGame()



class player:

    def __init__(self, nickname, level=0, score=0, ranking=0):
        self.nickname=nickname
        self.level=level
        self.score=score
        self.ranking=ranking

    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽는 메서드
    # set 메서드 - get 메서드
    def setNickname(self, nickName):
        self.nickName=nickName

    def setLevel(self, level):
        self.level=level

    def setScore(self, score):
        self.score=score

    def setRanking(self, ranking):
        self.ranking=ranking

    def setUpdate(self, level, score, ranking):
        self.level = level
        self.score = score
        self.ranking = ranking

    def getNickName(self): return self.nickName

    def getLevel(self): return self.level

    def getScore(self): return self.score

    def getRanking(self): return self.ranking