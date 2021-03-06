import sys

input = sys.stdin.readline


def solution(N, C, arr):
    arr = sorted(arr)
    start = 1
    end = arr[N - 1] - arr[0]
    mid = (start + end) // 2
    result = 0

    while start <= end:
        mid = (start + end) // 2
        frontHouse = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= frontHouse + mid:
                count += 1
                frontHouse = arr[i]

        if count >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)


if __name__ == "__main__":
    N, C = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(int(input().strip()))
    solution(N, C, arr)
