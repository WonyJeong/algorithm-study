import sys
from collections import deque


def MilkVisit(A, B, C):
    queue = deque([A])
    visit = [False for _ in range(N+1)]
    visit[A] = True
    while queue:
        q = queue.pop()
        for i in edge[q]:
            if home[i-1] == C and visit[i] == False:
                visit[i] = True
                queue.append(i)
    return visit


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys
    N, M = map(int, input().strip().split())
    home = input().strip()
    edge = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x, y = map(int, input().strip().split())
        edge[x].append(y)
        edge[y].append(x)

    friend = []
    for _ in range(M):
        A, B, C = map(str, input().strip().split())
        friend.append((int(A), int(B), C))

    result = ""
    visit = [False for _ in range(N+1)]
    for A, B, C in friend:
        if home[A-1] == C or home[B-1] == C:
            result += "1"
        else:
            if visit[A]:
                if visit[B]:
                    result += "0"
                else:
                    result += "1"
            else:
                visit = MilkVisit(A, B, home[A-1])
                if visit[B]:
                    result += "0"
                else:
                    result += "1"
    print(result)
