# LIC O(nlogn)
import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution(N, arr):
    answer = []
    lis = [arr[0]]
    index = [0]

    for i in range(1, N):
        if lis[len(lis) - 1] < arr[i]:
            lis.append(arr[i])
            index.append(len(lis) - 1)
        else:
            idx = bisect_left(lis, arr[i])
            lis[idx] = arr[i]
            index.append(idx)

    print(len(lis))
    cursor = len(lis) - 1
    for i in range(N - 1, -1, -1):
        if index[i] == cursor:
            answer.append(i)
            cursor -= 1

    for i in sorted(answer):
        print(arr[i], end=" ")


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)
