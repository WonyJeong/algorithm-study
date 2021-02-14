#1051
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    '''
    N = 행 수
    M = 열 수
    '''
    square = [list(map(int,input().strip())) for _ in range(N)]
    
    flag = False
    for i in range(M, 0, -1):
        if flag:
            break
        for j in range(N+1-i):
            if flag:
               break
            for k in range(M+1-i):
                if square[j][k] == square[j+i-1][k] == square[j+i-1][k+i-1] == square[j][k+i-1]:
                    answer = i
                    flag = True
                    break
    print(answer**2)