from collections import deque
import sys

input = sys.stdin.readline


def dfs(start):
    global visit
    global job
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in job[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    job = [[]]
    for _ in range(n):
        job.append(list(map(int,input().strip().split()))[1:])
    
    print(job)
    d = [0 for _ in range(n+1)]
    count = 0
    for i in range(1,n+1):
        visit = [0 for i in range(n+1)]
        if dfs(i):
            count += 1
    print(count)