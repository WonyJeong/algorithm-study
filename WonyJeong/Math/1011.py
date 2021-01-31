import sys

input = sys.stdin.readline


def getTurn(dist):
    ct = 0
    move = 1
    reducer = 0

    while reducer < dist:
        ct += 1
        reducer += move
        if ct % 2 == 0:
            move += 1
    print(ct)


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(0, T):
        x, y = map(int, input().strip().split())
        getTurn(y - x)
