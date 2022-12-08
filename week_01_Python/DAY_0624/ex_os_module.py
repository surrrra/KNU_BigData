# File & Dir 관련 모듈
# -----------------------------------------------
import os
import os.path as path

# 특정 "폴더" 존재 여부 체크 => 폴더 없으면 폴더 생성하기
DIR_PATH='./Image/jpg'
#print(path.exists(DIR_PATH))    # 경로가 존재하는지 체크

if not path.exists(DIR_PATH):
    #os.mkdir(DIR_PATH)          # mkdir은 폴더 한 개를 만들어줌
    os.makedirs(DIR_PATH)       # 하위 폴더까지 생성할 때 makedirs
# 만약에 './Image/jpg/01'이면 Image/jpg 폴더까지 있고 01이 없으니까 makedirs 아니고 mkdir 써야함

# 특정 파일 존재 여부 체크 -------------------------------------------------------------------------
DATA_FILE=DIR_PATH+'/flower.jpg'
if not path.exists(DATA_FILE):
    print('파일 없음')


# 특정 경로 안에 존재하는 내용 리스트화 ---------------------
dataList=os.listdir('./AddressBook')
print(dataList)


# 시간 관련 모듈(p.253) ------------------------------------------
import time as t
# 현재 시간
print(t.time()) # 현재 시간을1970/1/1 00:00:00을 기준으로 지난 시간을 초단위로 돌려줌
print(t.localtime(t.time())) # 연도, 월, 일, 시 분, 초, ... 의 형태로 바꾸어줌
curTime=t.localtime(t.time())
print(curTime.tm_year, curTime.tm_hour, curTime.tm_wday)
# 2022-06-24 2022/06/24 24/06/2022

for num in range(10):
    t.sleep(1.0)   # 1초에 하나씩
    print('|||', end='')
