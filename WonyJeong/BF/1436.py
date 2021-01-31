import sys

input = sys.stdin.readline


def sixsixsix(N):
    ct = 0
    i = 0
    while True:
        i += 1
        if str(i).find("666") != -1:
            ct += 1
            if ct == N:
                print(i)
                break


if __name__ == "__main__":
    N = int(input().strip())
    sixsixsix(N)
