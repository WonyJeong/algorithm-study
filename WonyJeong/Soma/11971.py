import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr1 = [0 for _ in range(100)]
    arr2 = [0 for _ in range(100)]
    cursor = 0
    for _ in range(N):
        dist, speed = map(int, input().strip().split())
        for i in range(cursor, cursor + dist):
            arr1[i] = speed
        cursor += dist
    cursor = 0
    for _ in range(M):
        dist, speed = map(int, input().strip().split())
        for i in range(cursor, cursor + dist):
            arr2[i] = speed
        cursor += dist
    max_ = max([i - j for i, j in zip(arr2, arr1)])
    if max_ > 0:
        print(max_)
    else:
        print(0)
