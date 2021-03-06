import sys

input = sys.stdin.readline


def devide(x, y, size):
    global arr, answer
    temp = arr[x][y]
    flag = True
    for i in range(x, x + size):
        if flag == True:
            for j in range(y, y + size):
                if arr[i][j] != temp:
                    flag = False

    if flag == True:
        answer[temp + 1] += 1

    if flag == False:
        nextSize = size // 3
        if nextSize >= 1:
            devide(x + nextSize * 0, y + nextSize * 0, nextSize)
            devide(x + nextSize * 0, y + nextSize * 1, nextSize)
            devide(x + nextSize * 0, y + nextSize * 2, nextSize)

            devide(x + nextSize * 1, y + nextSize * 0, nextSize)
            devide(x + nextSize * 1, y + nextSize * 1, nextSize)
            devide(x + nextSize * 1, y + nextSize * 2, nextSize)

            devide(x + nextSize * 2, y + nextSize * 0, nextSize)
            devide(x + nextSize * 2, y + nextSize * 1, nextSize)
            devide(x + nextSize * 2, y + nextSize * 2, nextSize)


def solution(N, arr):
    devide(0, 0, N)
    print("\n".join(map(str, answer)))


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    answer = [0, 0, 0]
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, arr)
