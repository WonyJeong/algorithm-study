import sys

input = sys.stdin.readline


def cumSum(N):
    cum = 1
    i = 0
    while True:
        cum += 6 * (i)
        if N <= cum:
            break
        i += 1
    print(i + 1)


if __name__ == "__main__":
    answer = 0
    N = int(input().strip())
    cumSum(N)