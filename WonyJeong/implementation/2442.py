import sys

input = sys.stdin.readline


def drawStar(N):
    space = N - 1
    star = 1
    offset = -2
    for i in range(0, N):
        for k in range(space):
            print(" ", end="")

        for k in range(star):
            print("*", end="")

        space += offset // 2
        star -= offset

        print()


if __name__ == "__main__":
    N = int(input().strip())
    drawStar(N)