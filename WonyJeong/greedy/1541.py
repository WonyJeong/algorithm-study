import sys

input = sys.stdin.readline


def getMin(N, arr):
    answer = 0
    arr = sorted(arr, reverse=True)

    for i in range(0, len(arr)):
        if N == 0:
            break

        if arr[i] <= N:
            answer += N // arr[i]
            N = N % arr[i]

    print(answer)


if __name__ == "__main__":
    arr = []
    T, N = map(int, input().strip().split())
    for i in range(0, T):
        arr.append(int(input().strip()))

    getMin(N, arr)
