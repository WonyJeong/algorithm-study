#1051
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    '''
    N = 행 수
    M = 열 수
    가능한 가장 큰 정사각형의 한 변의 길이는 N,M중에 작은 값.
    '''
    square = [list(map(int,input().strip())) for _ in range(N)]

    sideLength = min(N,M)
    answer = 0

    for i in range(N):
        for j in range(M):
            for k in range(1,sideLength):
                if i+k < N and j+k < M :
                    if square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]:
                        if answer < k:
                            answer = k
    print((answer+1)**2)