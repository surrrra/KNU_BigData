#----------------------------------------------------------------------------------------
# 연애성향 테스트 (적극적/소극적)
#----------------------------------------------------------------------------------------
PATH=r'C:/Users/User/Desktop/second/'       # 저장된 파일 경로
#----------------------------------------------------------------------------------------
# 기    능 : 연애성향 테스트 점수 도출
# 함 수 명 : Loving_Tendencies_Score
# 파라미터 : 없음
# 반 환 값 : total
#----------------------------------------------------------------------------------------
def Loving_Tendencies_Score():
    total = 0               # 초기 점수
    for i in range(1,4):
        while True:
            with open(PATH + '연애성향' + str(i) + '.txt', 'r', encoding='utf-8') as f:
                print(f.read())
                a = int(input("선택지를 입력해 주세요: "))
                if a == 1:
                    total += 0
                    break      # while문을 빠져 나간다.
                elif a == 2:
                    total += 1
                    break
                else:
                    print('잘못된 번호입니다. 다시 입력하세요.')
    return total
#----------------------------------------------------------------------------------------
# 기    능 : 점수에 대한 해당 값으로 결과를 도출
# 함 수 명 : Loving_Tendencies_finish
# 파라미터 : total
# 반 환 값 : 없음
#----------------------------------------------------------------------------------------
def Loving_Tendencies_finish(total):    # 점수를 매개변수로 넣는다.
    if 0<=total<=1:                     # 점수에 해당 구간을 찾는다.
        with open(PATH + 'passive.txt', 'r', encoding='utf-8') as f:
            x=f.read()                      # 경로에 있는 텍스트 파일을 읽고 변수 x에 저장한다.
            with open(PATH + 'all_result.txt','w',encoding='utf-8') as fi:
                fi.write(x)                 # 최종 파일에 읽어들인 x 내용을 입력한다.
    elif 2<=total<=3:
        with open(PATH + 'active.txt', 'r', encoding='utf-8') as f:
            x = f.read()
            with open(PATH + 'all_result.txt', 'w', encoding='utf-8') as fi:
                fi.write(x)
#----------------------------------------------------------------------------------------

s=Loving_Tendencies_Score()
Loving_Tendencies_finish(s)



# 연애성향 테스트 (계획적/즉흥적)
# -------------------------------------------------------------------------------------------------
# 함수 기능 : 질문을 불러와서 대답 입력받기
# 함수명 : getAnswer
# 파라미터 : 없음
# 반환값 : 점수 합계 -> total
def getAnswer():
    total=0
    for i in range(4, 7): # 3문제
        with open(PATH+'\\'+'연애성향'+str(i)+'.txt', mode='r', encoding='utf-8') as f:
            print(f.read()) # 파일 열어서 각 문제 불러오기
            while True:  # 1, 2번 외에 다른 문자를 입력하면 질문 다시 불러오기
                answer = input("선택지를 입력해 주세요: ")
                if answer in ['1', '2']:
                    if answer=='1': total+=1
                    else: total+=0
                    break
                else: print('잘못된 번호입니다. 다시 입력하세요.')
    return total


# -------------------------------------------------------------------------------------------------
# 기능 : 결과를 불러오는 함수
# 함수명 : love_result
# 파라미터 : plan_type => J or P
# 반환값 : love_result_J / love_result_P에 적혀 있는 내용
def love_result(plan_type):
    with open(PATH+'\\'+'love_result_'+plan_type+'.txt', mode='r', encoding='utf-8') as f:
        return f.read()
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# 기능 : 결과를 파일에 저장하고 출력하는 함수
# 함수명 : print_result
# 파라미터 : total
# 반환값 : 없음
def print_result(total):
        if total>=2:
            with open(PATH+'\\'+'all_result.txt', mode='a', encoding='utf-8') as f:
                f.write('\n'+love_result('J'))
        else:
            with open(PATH+'\\'+'all_result.txt', mode='a', encoding='utf-8') as f:
                f.write('\n'+love_result('P'))
        # with open(PATH+'\\'+'all_result.txt', mode='r', encoding='utf-8') as result:
        #     print(result.read())
# ------------------------------------------------------------------------------------------

print_result(getAnswer())




#연애 성향
#-----------------------------------
# 함 수 명 : loveStyle
# 파라미터 : 없음
# 반 환 값 : count 결과 출력

def loveStyle():
    count = 0
    for i in range(1,4):
        with open(PATH+'\\d'+str(i)+'.txt',mode='r',encoding='utf-8') as f:
            print(f'{f.read()}')
        while True:
            a=int(input("선택지를 입력해 주세요: "))
            if a == 2 : count+=1
            else : count+=0
            break
    return count

#------------------------------------------------------
# 기    능 : 결과를 불러오는 함수
# 함 수 명 : call_Info
# 파라미터 :
# 반 환 값: 없음
# def call_Info(planType):
#     with open(DIR_PATH+'\\'+planType+'.txt', mode='r',encoding='utf-8')as f:
#         return f.read()
 #----------------------------------------------------


#------------------------------------------------------
# 기   능 : 질문 및 대답 입력 함수
# 함 수 명: printImage
#  파라미터: count
# 반 환 값: 없음
def printImage(count):
    if 0 <= count <= 1:
        with open(PATH+'\\'+'3.txt', mode='r', encoding='utf-8') as f:
            result=f.read()
        with open(PATH+'\\'+'all_result.txt', mode='a', encoding='utf-8') as f2:
            f2.write(result)

    elif count == 2:
        with open(PATH+'\\'+'2.txt', mode='r', encoding='utf-8') as f:
            result=f.read()
        with open(PATH+'\\'+'all_result.txt', mode='a', encoding='utf-8') as f2:
            f2.write(result)


    elif count == 3:
        with open(PATH+'\\'+'1.txt', mode='r', encoding='utf-8') as f:
            result=f.read()
        with open(PATH+'\\'+'all_result.txt', mode='a', encoding='utf-8') as f2:
            f2.write(result)



printImage(loveStyle())

print('\n당신의 결과는!')
with open(PATH + '\\' + 'all_result.txt', mode='r', encoding='utf-8') as f:
    print(f.read())