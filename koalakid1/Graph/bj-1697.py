import sys
import math
from collections import deque


def BFS():
    queue = deque([N])
    visited = [0] * 100001
    visited[N] = 1
    while queue:
        q = queue.popleft()
        if q == K:
            print(visited[q]-1)
            break

        for i in (q-1, q+1, q*2):
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[q] + 1
                queue.append(i)


if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    BFS()
