#2178
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def BFS(maze):
    queue = [[0,0]]

    while len(queue) > 0 :
        y, x= queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4) :
            nearX = x + dx[k]
            nearY = y + dy[k]

            if 0 <= nearX < M and 0 <= nearY < N:
                if maze[nearY][nearX] == 1:
                    queue.append([nearY, nearX])
                    maze[nearY][nearX] = maze[y][x]+1

    return maze[N-1][M-1]


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    maze = [ list(map(int, input().strip())) for _ in range(N)]
    
    print(BFS(maze))
