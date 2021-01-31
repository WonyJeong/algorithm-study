import sys

input = sys.stdin.readline


def fac(i, N, val):
    if N == 0:
        print(1)
        return

    if i == N:
        print(val)
        return

    fac(i + 1, N, val * (i + 1))


if __name__ == "__main__":
    N = int(input().strip())
    fac(1, N, 1)
