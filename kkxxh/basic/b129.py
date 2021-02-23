#이진 검색 알고리즘의 실행 과정을 출력

from typing import Any,Sequence

def bin_search(a: Sequence, key:Any) -> int:
    """시퀀스a에서 key와 일치하는 원소를 이진 검색 (실행과정을 출력)"
    pl = 0
    pr = len(a)-1

    print('  |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4*len(a)+2)*'-')

    while True :
        pc = (pl + pr)//2

        print('  |', end='')
        if pl != pc :
            print((pl*4+1)* ' ' + ' <-' + ((pc-pl)*4)*' '+ '+', end='')
        else :
            print((pc*4 +1) *' ' + '<+', end='')
        if pc != pr :
            print(((pr-pc)*4-2)* ' '+ '->')
        else :
            print('->')
        
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4', end='')
        print('\n  |')

        if a[pc] == key :
            return pc  #검색 성공
        elif a[pc] < key :
            pl = pc+1 #검색 범위 좁힘
        else :
            pr = pc -1 #검색 범위 좁힘
        if pl > pr :
            break
        return -1 # 검색 실패

if __name__ =='__main__':
    num = int(input('원소 수 입력 : '))
    x = [None]*num
    print('배열 데이터를 오름차순으로 입력하세요')

    x[0] = int(input('x[0]: '))
    for i in range(1, num):
        while True :
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]: #바로 직전에 입력하 원소값보다 큰 값 입력할 경우
                break

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = bin_search(x,ky)

    if idx == -1 :
        print('검색 실패')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')



#오류