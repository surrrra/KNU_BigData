menu='''
=== 나의 주소록 ===
    1. 전체보기
     2. 검 색
     3. 추 가
     4. 종 료
==================
'''
names=[]

def initApp():
    DIR_PATH=''
    import os
    os.

while True:
    print(menu)
    question=input("메뉴 선택 : ")
    if question in ('1', '2', '3', '4'):
        if question=='4': break  # 4번 입력하면 종료
        else:
            if question=='1':  # 전체보기
                print('전체보기')
                for name in names:   # names 리스트에 들어있는 정보 하나씩 반환
                    print(name)
            elif question=='3':    # 정보 추가하기
                data=input("이름, 전화번호, 지역 : ")
                data_split=data.split(',')
                result=[]
                # result에 strip한 이름, 전화번호, 지역 담기
                for d in data_split:
                    result.append(d.strip())
                filename=str(result[0]+'_'+result[1])    # filename = 홍길동_1111
                file_address=filename+'.txt'    # file_address = 홍길동_1111.txt
                with open(file_address, mode='w', encoding='utf-8') as file:
                    file.write(data)
                names.append(filename)
            elif question=='2':  # 검색하기
                sch=input("검색 단어 : ")
                for name in names:    # names 리스트에 들어있는 원소 하나씩 빼오기
                    if sch in name:   # 원소에 sch가 포함된다면
                        print(f'파일명 : {name}')
                        with open(name+'.txt', mode='r', encoding='utf-8') as file2:
                            read_file=file2.read()
                            print(read_file)


    else: print('1, 2, 3, 4 중에 선택하세요')