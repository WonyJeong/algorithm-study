import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j, L, R, arr, visited):
    stack = [[i, j]]
    union = []
    sum_ = 0
    ct = 0
    while stack:
        x, y = stack.pop()
        if visited[x][y] == False:
            visited[x][y] = True
            sum_ += arr[x][y]
            ct += 1
            union.append([x, y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                    if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                        stack.append([nx, ny])

    return sum_ // ct, union


def solution(N, L, R, arr):
    answer = 0
    flag = True

    while flag:
        flag = False
        visited = [[False for _ in range(N)] for _ in range(N)]
        unions = []
        averages = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:
                    average, union = dfs(i, j, L, R, arr, visited)
                    unions.append(union)
                    averages.append(average)

        for i in range(len(unions)):
            if len(unions[i]) > 1:
                flag = True
                for x, y in unions[i]:
                    arr[x][y] = averages[i]

        if flag == True:
            answer += 1
        else:
            break

    print(answer)


if __name__ == "__main__":
    N, L, R = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, L, R, arr)