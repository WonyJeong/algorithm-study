import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution(N, arr):
    answer = []
    s = -1
    e = len(arr) - 1
    arr = sorted(arr)
    while s < e:
        s += 1
        if arr[s] > 0 and s < len(arr) - 1:
            answer.append([arr[s], arr[s + 1], abs(arr[s] + arr[s + 1])])
            break

        lowerBoundValue = arr[s] * -1
        e = bisect_left(arr, lowerBoundValue)

        if e == len(arr):
            e -= 1
        e_ = e - 1
        if e_ > s:
            if abs(lowerBoundValue - arr[e]) > abs(lowerBoundValue - arr[e_]):
                e = e_
        if s == e:
            continue
        if s > e:
            break

        answer.append([arr[s], arr[e], abs(arr[e] + arr[s])])

    answer = sorted(answer, key=lambda x: x[2])
    # print(answer)
    print(answer[0][0], answer[0][1])


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)
