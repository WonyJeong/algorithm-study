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


def solution(N, arr):
    lis = [arr[0]]
    for i in range(1, N):
        if lis[len(lis) - 1] < arr[i]:
            lis.append(arr[i])
        else:
            lis[lowerbound(arr[i], lis)] = arr[i]

    print(len(lis))


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)
