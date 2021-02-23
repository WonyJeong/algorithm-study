import sys

input = sys.stdin.readline


def lowerbound(value, lis):
    l = 0
    r = len(lis) - 1
    ret = sys.maxsize
    while l <= r:
        mid = (l + r) // 2
        if lis[mid] >= value:
            if ret > mid:
                ret = mid
            r = mid - 1
        else:
            l = mid + 1
    return ret


def solution(N, arr1, arr2):
    order = [0 for _ in range(N + 1)]

    for i in range(N):
        order[arr2[i]] = i
    for i in range(N):
        arr1[i] = order[arr1[i]]

    lis = [arr1[0]]
    for i in range(1, N):
        if lis[len(lis) - 1] < arr1[i]:
            lis.append(arr1[i])
        else:
            lis[lowerbound(arr1[i], lis)] = arr1[i]

    print(len(lis))


if __name__ == "__main__":
    N = int(input().strip())
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    solution(N, arr1, arr2)
