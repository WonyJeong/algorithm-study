import sys
input = sys.stdin.readline
from collections import deque

def BFS(x,y):
    queue = deque([(x,y)])
    xm = [1,-1,0,0]
    ym = [0,0,1,-1]
    global s
    global n
    eat = 0
    size = 2
    time = 0
    stop = False
    result = 0
    visited = set()
    while queue:
        queue = deque(sorted(queue))
        length = len(queue)
        for _ in range(length):
            x,y = queue.popleft()
            visited.add((x,y))
            if 0 < s[x][y] < size:
                s[x][y] = 0
                eat += 1

                if eat == size:
                    eat = 0
                    size += 1
                queue = deque([(x,y)])
                visited = set()
                stop = True
                result = time
            for i in range(4):
                xn = x + xm[i]
                yn = y + ym[i]
                if 0 <= xn < n and 0 <= yn < n and (xn,yn) not in visited and s[xn][yn] <= size:
                    queue.append((xn,yn))
                    visited.add((xn,yn))
            if stop:
                stop = False
                break
        time += 1
    return result

if __name__ == "__main__":
    n = int(input())
    s = []
    check = False
    for i in range(n):
        a = list(map(int,input().strip().split()))
        if 9 in a:
            x = i
            y = a.index(9)
            a[y] = 0
        for j in a:
            if j == 1:
                check = True
        s.append(a)
    
    if check:
        print(BFS(x,y))
    else:
        print(0)
    