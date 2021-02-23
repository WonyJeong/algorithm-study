#10진수 정수값을 입력받아 2~36진수로 변환하여 출력
def card_conv(x: int, r: int) -> str:
    """정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d= ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')
    while x> 0 :
        print('  +' + (n+2) * '-')
        if x//r :
            print(f'{r:2} | {x // r:{n}d}... {x%r}')
        else :
            print(f'     {x // r:{n}d}... {x%r}')
        d += dchar[x%r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환')
    
    while True :
        while True :
            no = int(input('변환할 값으로 음이 아닌 정수 입력 : '))
            if no > 0 :
                break

        while True :
            cd = int(input('어떤 진수로 변환할까요? : '))
            if 2 <= cd <= 36 :
                break
        print(f'{cd}진수로는 {card_conv(no,cd)}입니다')

        retry = input('한번 더 변환할까요? (Y - 예 / N - 아니요) : ')
        if retry in {'N', 'n'} :
            break