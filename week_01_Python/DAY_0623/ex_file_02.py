# PATH => 경로
# - 절대경로 : 파일 및 폴더 존재하는 위치의 경로 ex) C:\Users\anece\....
#             근데 바탕화면에 있는거 같은거 찾으려면 어쩔 수 없이 절대경로 써야함
# - 상대경로 : 현재 코드 파일 기준으로 경로를 지정
#   . -> 현재 위치
#   .. -> 상위(한 단계 위)

file='../Data/home.html'
file='./html/home.html' # 둘 다 상대경로


# home.html 파일을 라인 단위로 읽어서 화면에 출력하기
filename='./html/home.html'
file=open(filename, mode='r', encoding='utf-8')

while True:
    data=file.readline()
    if not data: break
    data=data.strip()
    if len(data)>0 : print(f'line data => {data}') # 아무것도 없는 줄 없애기 위한 코드

file.seek(0)
data1=file.readline()
print(f'data1 => {data1}')
data2=file.readline()
print(f'data2 => {data2}')

file.seek(0)
datas=file.readlines()
print(f'datas => {datas}')
file.close()

# with ~ as 구문
with open(filename, mode='r', encoding='utf-8') as file:
    while True:
        data = file.readline()
        if not data: break
        data = data.strip()
        if len(data) > 0: print(f'line data => {data}')