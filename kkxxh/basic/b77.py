#시퀀스 원소의 최댓값 출력

from typing import Any, Sequence

def max_of(a: Sequence) -> Any :
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum :
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최댓값 구하기')
    num = int(input('원소 수 :'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값 입력하세요'))

    print(f'최댓값은 {max_of(x)}입니다')


# 스크립트 프로그램이 직접 실행될 때 변수 __name__ 은 '__main__'이다
# 스크립트 프로그램이 임포트될 때 변수 __name__은 원래의 모듈 이름