#16656
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    pack = 1
    
    if N <= 10:
        print(pack) #0~10까지는 1개의 스티커팩으로 표현 가능
    
    else: 
        '''
        11~110 : 2팩
        111~1110 : 3팩 
        같은 수를 두 번 쓰는 경우 스티커 팩의 수가 하나 증가
        '''
        while pack <= N :
            pack = str(pack)
            pack += '1' #'111'
            pack = int(pack) #111
    
        print(len(str(pack//10))) 
        #현재 card는 N보다 더 큰수 -> 자리수를 구하기 위해 10으로 나눔