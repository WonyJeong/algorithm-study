import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dangi(T, arr, i, j):
    answer = 0
    stack = [[i, j]]
    while stack:
        top = stack.pop()
        x = top[0]
        y = top[1]
        if arr[x][y] == 1:
            arr[x][y] += 1
            answer += 1
            for k in range(0, 4):
                if (
                    0 <= x + dx[k] < T
                    and 0 <= y + dy[k] < T
                    and arr[x + dx[k]][y + dy[k]] == 1
                ):
                    stack.append([x + dx[k], y + dy[k]])
    return answer


if __name__ == "__main__":
    answer1 = 0
    answer2 = []
    T = int(input().strip())
    arr = []
    for i in range(0, T):
        row = list(map(int, input().strip()))
        arr.append(row)

    for i in range(0, T):
        for j in range(0, T):
            if arr[i][j] == 1:
                answer1 += 1
                answer2.append(dangi(T, arr, i, j))
    print(answer1)
    print("\n".join(map(str, sorted(answer2))))
