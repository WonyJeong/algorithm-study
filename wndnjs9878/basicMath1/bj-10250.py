#10250
import sys
input = sys.stdin.readline
def solved(H, W, N):
    '''
    H : 호텔의 층수
    W : 각 층의 방 수 
    N : 몇 번째 손님인지
    '''
    if N%H != 0 :
        return f'{N%H}'+'{0:02d}'.format(int(N/H)+1)
    else :
        return str(H)+'{0:02d}'.format(int(N/H))

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(0,T) :
        H, W, N = map(int, input().strip().split())
        print(solved(H, W, N), end='\n')