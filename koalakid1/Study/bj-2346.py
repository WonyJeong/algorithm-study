import sys
from collections import deque


def fire():
    global number
    global N

    visited = [False for _ in range(N)]
    visited[0] = True
    visit = [1]

    for i in range(N-1):
        index = visit[i] - 1
        move = number[index]
        direction = 1 if move > 0 else -1
        go = 0
        while go < abs(move):
            index = (index + direction) % N
            if visited[index] == False:
                go += 1
        visit.append(index + 1)
        visited[index] = True

    print(" ".join(map(str, visit)))


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    number = list(map(int, input().strip().split()))
    fire()
