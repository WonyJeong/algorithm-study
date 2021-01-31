import sys

input = sys.stdin.readline


def fibonacci(x, y, i, N):
    if N == 0:
        print(0)
        return

    if N == 1:
        print(1)
        return

    if N == i:
        print(x + y)
        return

    fibonacci(y, x + y, i + 1, N)


if __name__ == "__main__":
    N = int(input().strip())
    fibonacci(0, 1, 2, N)
# 0  1  2  3  4  5  6  7   8   9   10
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
