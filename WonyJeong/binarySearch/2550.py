import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution(N, arr, arr2):
    arr1 = [0 for _ in range(N)]
    answer = []
    order = [0 for _ in range(N + 1)]
    for i in range(N):
        order[arr2[i]] = i
    for i in range(N):
        arr1[i] = order[arr[i]]

    lis = [arr1[0]]
    index = [0]

    for i in range(1, N):
        if lis[len(lis) - 1] < arr1[i]:
            lis.append(arr1[i])
            index.append(len(lis) - 1)
        else:
            idx = bisect_left(lis, arr1[i])
            lis[idx] = arr1[i]
            index.append(idx)

    print(len(lis))
    cursor = len(lis) - 1
    for i in range(N - 1, -1, -1):
        if index[i] == cursor:
            answer.append(i)
            cursor -= 1
    # answer = sorted(answer)
    temp = []
    for i in answer:
        temp.append(arr[i])

    for i in sorted(temp):
        print(i, end=" ")


if __name__ == "__main__":
    N = int(input().strip())
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    solution(N, arr1, arr2)
