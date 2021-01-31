import sys

input = sys.stdin.readline


def structNumber(N):
    start = 1

    while True:
        if start > N:
            print(0)
            break

        temp = 0
        for val in str(start):
            temp += int(val)

        if temp + start == N:
            print(start)
            break
        start += 1


if __name__ == "__main__":
    N = int(input().strip())
    structNumber(N)
