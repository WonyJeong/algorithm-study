#binary search
#배열의 데이터가 정렬되어 있어야 함
#선형 검색보다 빠르게 검색 가능

from typing import Any, Sequence

def bin_search(a: Sequence, key : Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색 """
    pl = 0 #왼쪽 끝으로 초기화
    pr = len(a)-1 #오른쪽 끝으로 초기화

    while True :
        pc = (pl + pr) //2 #중앙 인덱스
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

    if idx ==-1 :
        print('검색 실패')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')