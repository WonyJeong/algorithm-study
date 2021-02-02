import sys

input = sys.stdin.readline


def getTime(T, arr):
    arr = sorted(arr, key=lambda x: x[0])
    arr = sorted(arr, key=lambda x: x[1])
    answer = 0
    cursor = 0

    for i, j in arr:
        if i >= cursor:
            answer += 1
            cursor = j
    print(answer)
    print(arr)


if __name__ == "__main__":
    arr = []
    T = int(input().strip())
    for _ in range(T):
        cof = list(map(int, input().strip().split()))
        arr.append(cof)
    getTime(T, arr)
