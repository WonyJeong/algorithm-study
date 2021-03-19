import sys
from collections import deque 
input = sys.stdin.readline
        

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    graph = [input().strip() for _ in range(n)]

    visited = [[True] * m for _ in range(n)]
    can = [[True] * m for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                queue = deque([(i,j)])
                visit = [(i,j)]
                while queue:
                    x,y = queue.popleft()
                    if graph[x][y] == "U":
                        x -= 1
                    elif graph[x][y] == "R":
                        y += 1
                    elif graph[x][y] == "D":
                        x += 1
                    else:
                        y -= 1
                    if 0 <= x < n and 0 <= y < m and (x,y) not in visit:
                        if visited[x][y]:
                            visit.append((x,y))
                            queue.append((x,y))
                        else:
                            if can[x][y]:
                                for x,y in visit:
                                    result += 1
                                    visited[x][y] = False
                            else:
                                for x,y in visit:
                                    visited[x][y] = False
                    elif (x,y) in visit:
                        for x,y in visit:
                            visited[x][y] = False
                            can[x][y] = False
                    else:
                        for x,y in visit:
                            result += 1
                            visited[x][y] = False
    print(result)