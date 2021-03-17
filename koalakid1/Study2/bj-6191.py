import sys
from collections import deque 
input = sys.stdin.readline
        

if __name__ == "__main__":
    r,c = map(int,input().strip().split())
    graph = [input().strip() for _ in range(r)]

    visited = [[0 for _ in range(c)] for _ in range(r)]
    
    queue = deque([(0,0)])
    visited[0][0] = (-1,-1)
    xm = [1,-1,0,0]
    ym = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            xn = x + xm[i]
            yn = y + ym[i]
            if 0 <= xn < r and 0 <= yn < c and not visited[xn][yn] and graph[xn][yn] == ".":
                visited[xn][yn] = (x,y)
                queue.append((xn,yn))

    result = [(r,c)]
    x,y = visited[r-1][c-1]
    while x != -1 and y != -1:
        result.insert(0,(x+1,y+1))
        x,y = visited[x][y]
    
    for x,y in result:
        print(x,y)

