import sys

input = sys.stdin.readline


def minju(N, cross, l, r):
    min_ = sys.maxsize
    idx = 0

    lsum = 0
    rsum = sum(r)

    for i in range(0, N):
        rsum -= r[i]
        lsum += l[i]
        temp = cross[i] + rsum + lsum

        if min_ > temp:
            idx = i + 1
            min_ = temp

    print(idx, min_)


if __name__ == "__main__":
    N = int(input().strip())
    cross = list(map(int, input().strip().split()))
    l = [0] + list(map(int, input().strip().split()))
    r = [0] + list(map(int, input().strip().split()))

    minju(N, cross, l, r)