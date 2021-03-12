import sys

input = sys.stdin.readline


def recursive(x, y, size):
    global answer
    one = [[1 for _ in range(size)] for _ in range(size)]
    zero = [[0 for _ in range(size)] for _ in range(size)]

    partial = [row[y : y + size] for row in arr[x : x + size]]

    if partial == one:
        answer += "1"
    elif partial == zero:
        answer += "0"
    else:
        size = size // 2
        if size >= 1:
            answer += "("
            recursive(x, y, size)
            recursive(x, y + size, size)
            recursive(x + size, y, size)
            recursive(x + size, y + size, size)
            answer += ")"


def solution(N, arr):
    global answer
    answer = ""
    recursive(0, 0, N)
    print(answer)


if __name__ == "__main__":
    global arr
    answer = ""
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip())))

    solution(N, arr)