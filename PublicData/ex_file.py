# p.171
# 파일 읽고 쓰기 => 파일 입출력(I/O)
filename='mydata.txt'

# 파일 쓰기 ---------------------------
# (1) 파일 열기
# mode='w' => 파일 없으면 생성 후 쓰기
#          => 파일 있으면 내용 지우고 쓰기
#file=open(filename, mode='w', encoding='utf-8')
# mode='a' => append 약자
#          => 파일 없으면 생성 후 쓰기
#          => 파일 있으면 덧붙이기 즉 append
file=open(filename, mode='a', encoding='utf-8')
# (2) 파일에 데이터 쓰기
file.write('Good\n') # write는 줄바꿈이 안 됨.
file.write('Happy\n')
# (3) 파일 닫기 : 이거 까먹으면 안됨
file.close()

# 파일 읽기 ------------------------------------------
# mode='r' => read 약자, 기본값
# (1) 파일 열기
file=open(filename, mode='r')

# (2) 파일 읽기
data=file.read()   # .read()는 전체를 다 읽어옴
print(f'read data => {data}')
print(f'read data => {type(data)}')
data2=file.read()   # 아무것도 안 나옴
print(f'read data => {data2}, len => {len(data2)}')

# 파일을 읽으면 커서가 제일 뒤로 가는데 커서 뒤로 아무 글자가 없어서 read()를 한 번 더 하면 아무것도 안 나옴
file.seek(0)  # 커서를 0번 자리로 이동
data2=file.read()
print(f'read data2 => {data2}, len => {len(data2)}')

# 파일 포인트 제일 앞으로
file.seek(0)
# 파일에서 1줄 읽기. 줄바꿈문자까지가 한 줄
data3=file.readline()
print(f'data3 =>{data3}')
data3=file.readline()
print(f'data3 =>{data3}')
data3=file.readline()
print(f'data3 =>{data3}')

# 1줄씩 읽어서 리스트에 담아서 가져오기
data4=file.readlines()
print(f'data4 =>{data4}')

data=file.read(4) # 글자 4개 읽어옴. \n도 하나의 문자로 취급한다

# (3) 파일 닫기
file.close()



