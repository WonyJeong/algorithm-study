import sys

input = sys.stdin.readline


def fn(n):
    n_ = list(str(n))
    temp = ""
    for i in range(0, len(n_)):
        temp += str(9 - int(n_[i]))
    return int(temp)


def lovely(n):
    length = len(str(n))
    center = (10 ** length) // 2

    answer = []

    if n <= center:
        print(fn(n) * n)
    else:
        print(fn(center) * center)


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        lovely(int(input().strip()))
