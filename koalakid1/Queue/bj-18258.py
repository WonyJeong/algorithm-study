import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque([])

for _ in range(N):
    item = list(map(str, input().strip().split()))
    action = item[0]
    if action == "push":
        queue.append(item[1])
    if action == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    if action == "size":
        print(len(queue))
    if action == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    if action == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    if action == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
