import sys

input = sys.stdin.readline


def solution(N, C, arr):
    arr = sorted(arr)
    # 가장 낮은 좌표와 그 다음으로 낮은 좌표의 차이
    start = arr[1] - arr[0]
    # 가장 높은 좌표와 가장 낮은 좌표의 차이
    end = arr[-1] - arr[0]

    result = 0
    while start <= end:
        mid = (start + end) // 2  # 해당 gap
        old = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= old + mid:  # gap 이상
                count += 1
                old = arr[i]

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
