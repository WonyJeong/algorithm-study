#1303
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def BFS(war, cnt, x, y, element):
    war[y][x] = 'V'
    queue = []
    queue.append((x,y))

    while len(queue) > 0 :
        x, y = queue.pop()
        for k in range(4) :
            nearX = x + dx[k]
            nearY = y + dy[k]

            if 0 <= nearX < N and 0<= nearY < M:
                if war[nearY][nearX] == element:
                    cnt += 1
                    war[nearY][nearX] = 'V'
                    queue.append((nearX, nearY))
    return cnt

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    war = [list(input().strip()) for _ in range(M)]

    temp = ['W', 'B']
    for element in temp :
        answer = 0
        for i in range(M):
            for j in range(N):
                if war[i][j] == element:
                    num = BFS(war, 1, j, i, element)
                    if num != 0 :
                        answer += num**2
        print(answer, end=' ')