#1904
import sys
input = sys.stdin.readline

def solution(N):
    tile = [1,2]
    for i in range(2,N):
        tile.append((tile[i-1] + tile[i-2])%15746)
    # 15746으로 나눈값을 저장해야지 메모리 초과나지 않음
    '''
    tile[0] = 0
    tile[1] = [1] = 1
    tile[2] = [00,11] =2
    tile[3] 100 111 001 = 3
    tile[4] = 5
    1001     
    1111     
    0000     
    1100     
    0011 
    tile[5] = 8
    00001  
    00100
    00111    
    10000     
    10011
    11001 
    11100    
    11111
    
    => tile[N] = tile[N-1] + tile[N-2]
    '''
    
    return tile[N-1]


if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))