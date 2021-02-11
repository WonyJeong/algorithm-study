#1696 BFS의 깊이 구하는 문제
import sys
from collections import deque
input = sys.stdin.readline

def BFS(N,K):
    queue = deque()
    queue.append(N)
    visited = [0]*100001

    while len(queue) > 0 :
        position = queue.popleft()
        if position == K :
            return visited[position]
        for next in (position-1, position+1, 2*position):
            if 0 <= next < 100001 and visited[next] == 0:
                queue.append(next)
                visited[next] = visited[position]+1


if __name__ == '__main__':
    N, K = map(int,input().strip().split())
    print(BFS(N,K))