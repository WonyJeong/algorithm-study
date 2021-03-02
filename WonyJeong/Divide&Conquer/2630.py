import sys

input = sys.stdin.readline


def devide(x, y, size):
    global arr, answer
    partial = [row[y : y + size] for row in arr[x : x + size]]
    zero = [[0 for _ in range(size)] for _ in range(size)]
    one = [[1 for _ in range(size)] for _ in range(size)]

    if partial == zero:
        answer[0] += 1
        return

    if partial == one:
        answer[1] += 1
        return

    nextSize = size // 2
    if nextSize >= 1:
        devide(x, y, size // 2)
        devide(x + size // 2, y, size // 2)
        devide(x, y + size // 2, size // 2)
        devide(x + size // 2, y + size // 2, size // 2)


def solution(N, arr):
    devide(0, 0, N)
    print("\n".join(map(str, answer)))


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    answer = [0, 0]
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, arr)
