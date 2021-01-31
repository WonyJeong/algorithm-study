import sys

input = sys.stdin.readline


def getFraction(N):
    cumSum = 0
    row = 1
    while True:
        cumSum += row
        if N <= cumSum:
            if row % 2 == 0:
                right = 1 + (cumSum - N)
                left = row - (cumSum - N)
            else:
                left = 1 + (cumSum - N)
                right = row - (cumSum - N)

            print(f"{left}/{right}")
            break

        row += 1


if __name__ == "__main__":
    answer = 0
    N = int(input().strip())
    getFraction(N)
