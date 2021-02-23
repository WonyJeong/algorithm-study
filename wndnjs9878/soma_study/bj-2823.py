#2823
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solved(R, C, downtown) :
    for i in range(R) :
        for j in range(C):
            if downtown[i][j] == '.':
                cnt = 0
                for k in range(4):  
                    nearX = i + dx[k]
                    nearY = j + dy[k]
                    if 0 <= nearX < R and 0 <= nearY < C and downtown[nearX][nearY] == '.':
                        cnt += 1
                if cnt == 0 or cnt == 1:
                    return 1
                else :
                    continue
    return 0


if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    downtown = [list(input().strip()) for _ in range(R)]
    '''
    R : 행
    C : 열
    '''
    print(solved(R, C, downtown))