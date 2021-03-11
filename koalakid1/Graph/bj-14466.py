import sys
from collections import deque

def draw(i,j,area):

    rm = [1,-1,0,0]
    cm = [0,0,1,-1]

    queue = deque([(i,j)])
    graph[i][j] = area
    count = 0
    while queue:
        r,c = queue.popleft()
        if location[r][c] == 1:
            count += 1
        for k in range(4):
            rn = r + rm[k]
            cn = c + cm[k]
            if 0 <= rn < n and 0 <= cn < n and graph[rn][cn] == -1:
                if (r,c) not in road or ((r,c) in road and (rn,cn) not in road[(r,c)]):
                    queue.append((rn,cn))
                    graph[rn][cn] = area
    return count

def solution():
    result = []
    area = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                result.append(draw(i,j,area))
                area += 1

    answer = 0
    for i in range(len(result)-1):
        answer += result[i] * (sum(result[i+1:]))
    print(answer)

if __name__ == "__main__":
    input = sys.stdin.readline
    global road, graph, location
    n,k,r = map(int,input().strip().split())
    road = {}
    for _ in range(r):
        r1,c1,r2,c2 = map(int,input().strip().split())
        if (r1-1,c1-1) not in road:
            road[(r1-1,c1-1)] = [(r2-1,c2-1)]
        else:
            road[(r1-1,c1-1)].append((r2-1,c2-1))
        
        if (r2-1,c2-1) not in road:
            road[(r2-1,c2-1)] = [(r1-1,c1-1)]
        else:
            road[(r2-1,c2-1)].append((r1-1,c1-1))
    
    location = [[0]* n for _ in range(n)]
    for _ in range(k):
        r,c = map(int,input().strip().split())
        location[r-1][c-1] = 1

    graph = [[-1] * n for _ in range(n)]

    solution()