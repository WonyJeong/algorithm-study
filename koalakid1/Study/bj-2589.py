from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    graph = [input().strip() for _ in range(n)]
    visited = [[True for _ in range(m)] for _ in range(n)]
    xm = [1,-1,0,0]
    ym = [0,0,1,-1]
    result = 0
    for i in range(n):
        for j in range(m):
            count = -1
            if graph[i][j] == "L" and visited[i][j]:
                visited[i][j] = False
                queue = deque([(i,j)])
                visit = set([(i,j)])
                while queue:
                    lenq = len(queue)
                    for _ in range(lenq):
                        x,y = queue.popleft()
                        for k in range(4):
                            xn = x + xm[k]
                            yn = y + ym[k]
                            if 0<=xn<n and 0<=yn<m and (xn,yn) not in visit and graph[xn][yn] == "L":
                                visit.add((xn,yn))
                                queue.append((xn,yn))
                    count += 1
                if count > result:
                    visited[x][y] = False
                    result = count
    print(result)
