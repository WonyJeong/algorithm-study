import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = input().strip()
    length = len(N)
    if int(N) >= int("1" * len(N)):
        print(length)
    else:
        if N == "0":
            print(length)
        else:
            print(length - 1)
