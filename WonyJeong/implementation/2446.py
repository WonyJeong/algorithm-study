import sys

input = sys.stdin.readline


def drawStar(N):
    space = 0
    star = 2 * N - 1
    offset = -2
    for i in range(0, 2 * N - 1):
        for k in range(space):
            print(" ", end="")

        for k in range(star):
            print("*", end="")

        # for k in range(space):
        #     print(" ", end="")

        if star == 1:
            offset *= -1

        space -= offset // 2
        star += offset

        print()


if __name__ == "__main__":
    N = int(input().strip())
    drawStar(N)