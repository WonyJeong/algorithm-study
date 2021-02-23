#선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any):
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq) #seq복사
    a.append(key) #보초 key 추가

    i = 0
    while True :
        if a[i] == key :
            break #검색에 성공하면 while문 종료
        i+= 1
    #원래 데이터인지 보초인지 판단
    return -1 if i == len(seq) else i #검색 성공하면 인덱스 반환, 추가한 보초key(len(seq)라면 검색 실패

if __name__ == "__main__":
    num = int(input("원소 수 입력 :" ))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}] :'))

    ky = int(input('검색할 값 입력 : '))

    idx = seq_search(x,ky)

    if idx == -1 :
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else : print(f'검색값은 x[{idx}]에 있습니다.')