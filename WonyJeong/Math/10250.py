import sys

input = sys.stdin.readline


def temp(h, w, n):
    row = n // h + 1
    col = n % h

    if col == 0:
        row -= 1
        col = h

    print(col * 100 + row)


if __name__ == "__main__":
    answer = 0
    T = int(input().strip())
    for i in range(0, T):
        H, W, N = map(int, input().strip().split())
        temp(H, W, N)
