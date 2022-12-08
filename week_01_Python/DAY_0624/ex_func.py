YEAR=2022

def printYear():
    print(f'올해는 {YEAR}년')

if __name__ == '__main__':
    for i in range(5): printYear()
    print(f'[ex_func] __name__ => {__name__}')


# 현재 실행 중인 파일은 __name__이 __main__으로 나옴(p.211)



