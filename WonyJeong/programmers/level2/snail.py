def direction(x, y, i):

    if i % 3 == 0:
        x += 1
    elif i % 3 == 1:
        y += 1
    elif i % 3 == 2:
        x -= 1
        y -= 1

    return x, y


def solution(n):
    answer = []

    arr = []
    idx = 1

    x = -1
    y = 0
    for i in range(1, n + 1):
        arr.append([0 for _ in range(i)])

    for i in range(n):
        for j in range(i, n):
            x, y = direction(x, y, i)
            arr[x][y] = idx
            idx += 1

    for a in arr:
        answer += a

    return answer


if __name__ == "__main__":
    print(solution(6))