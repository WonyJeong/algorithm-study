#1012
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def BFS(cabbagePatch, cnt, x, y):
    cabbagePatch[y][x] = 0
    queue = []
    queue.append((x,y))

    while len(queue) > 0 :
        x, y = queue.pop()
        for k in range(4) :
            nearX = x + dx[k]
            nearY = y + dy[k]

            if 0 <= nearX < M and 0<= nearY < N:
                if cabbagePatch[nearY][nearX] == 1:
                    cnt += 1
                    cabbagePatch[nearY][nearX] = 0
                    queue.append((nearX, nearY))
        
    return cnt

if __name__ == '__main__':
    T = int(input().strip())

    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        numberOfbugs = []
        cabbagePatch = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            x, y = map(int, input().strip().split())
            cabbagePatch[y][x] = 1
        
        for i in range(N):
            for j in range(M):
                if cabbagePatch[i][j] == 1:
                    numberOfbugs.append(BFS(cabbagePatch,1,j,i))

        print(len(numberOfbugs))

