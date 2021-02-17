import sys

input = sys.stdin.readline


def findSeconMaxNumber(a, b, c):
    answer = [a, b, c]
    answer = sorted(answer)

    print(answer[1])
    print("*" * 3)


if __name__ == "__main__":
    a, b, c = map(int, input().strip().split())
    findSeconMaxNumber(a, b, c)
