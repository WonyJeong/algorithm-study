#1260
import sys

input = sys.stdin.readline
N, M, V = map(int, input().strip().split())

for i in range(N + 1):
    s = [[0] * (N + 1)]
for i in range(N + 1):    
    visit = [0]

for i in range(M):
    x, y = map(int, input().strip().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(V)
print(" ")
bfs(V)


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, N + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

#runtime error
#2/13-14 DFS,BFS study