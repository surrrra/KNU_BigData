# 사용자가 입력한 댓글을 파일로 저장하기
# [조건]
# - 키보드로 댓글 입력 받기
# - 입력 받은 댓글 누적하기
# - 댓글 입력 종료 조건으로 q 또는 Q 입력시 댓글 입력 종료 (무한반복)
# input() : 내장함수
# - 매개변수 : 입력받고 싶은 데이터 요청 메시지 => str타입으로 들어옴
# - 결과 : 입력받은 데이터 => str 타입

filename='comment.txt'
file = open(filename, 'a', encoding='utf-8')
while True:
    comment=input("댓글을 입력하세요. q 또는 Q 입력시 종료됩니다 : ")
    if comment=='q' or comment=='Q': break # if comment in ['q', 'Q']:
    file.write(comment)
    file.write('\n')
file.close()

f=open(filename, 'r', encoding='utf-8')
data=f.read()
print(data)
f.close()

# 강사님 ver
with open(filename, mode='a', encoding='utf-8') as f:
    while True:
        txt=input("댓글 입력 : ")
        if txt in ['q', 'Q']: break
        print(f'txt =>{txt}')
        f.write(txt+'\n')

# ------------------------------------------------------------
# 문제 2번
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함수명 : fileCopy
# - 매개변수 : 파일명
# - 반환값 : 없음
#
filename='./html/home.html'
def fileCopy(filename):
    with open(filename, mode='r', encoding='utf-8') as file1:
        with open('home.txt', mode='a', encoding='utf-8') as file2:
            while True:
                data1=file1.readline()
                if not data1: break
                file2.write(data1)

fileCopy(filename)


# 강사님 ver
def fileCopy(filename):
    srcFile=open(filename, mode='r', encoding='utf-8')
    data=srcFile.read()
    srcFile.close()

    # 복사본 파일에 데이터 쓰기
    #filename=filename.split('/')[2].split('.')[0]+'.txt'
    filename=filename[:filename.rindex(".")]+'.txt'
    desFile=open(filename, mode='w', encoding='utf-8')
    desFile.write(data)
    desFile.close()

fileCopy(filename)