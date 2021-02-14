import sys

input = sys.stdin.readline


def deguldegul(N):
    while N != 0:
        result = 0
        text = []
        for i in range(N):
            line = list(input().strip())
            for j in range(result, len(line) + 1):
                if j == len(line) or line[j] == " ":
                    result = j
                    break

        print(result + 1)

        N = int(input().strip())


if __name__ == "__main__":
    N = int(input().strip())
    deguldegul(N)