import sys

input = sys.stdin.readline


def solution(K, N, arr):
    l, r = 1, max(arr)
    while l <= r:
        mid = (l + r) // 2
        temp = 0
        for lan in arr:
            temp += lan // mid

        if temp >= N:
            l = mid + 1
        else:
            r = mid - 1
    print(r)


if __name__ == "__main__":
    K, N = map(int, input().strip().split())
    arr = []
    for _ in range(K):
        arr.append(int(input().strip()))
    solution(K, N, arr)
