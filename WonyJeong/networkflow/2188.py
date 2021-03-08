import sys

input = sys.stdin.readline


def dfs(n, flow):
    if visited[n]:
        return 0

    visited[n] = True
    for i in flow[n]:
        if not left[i] or dfs(left[i], flow):
            left[i] = n
            return 1


def solution(flow):
    global left, visited
    answer = 0

    left = [0 for _ in range(201)]

    for i in range(1, N + 1):
        visited = [False for _ in range(201)]
        if dfs(i, flow):
            answer += 1
    print(answer)


if __name__ == "__main__":
    N, M = map(int, input().split())
    flow = [[]]
    for i in range(N):
        flow.append(list(map(int, input().strip().split()))[1:])

    solution(flow)
