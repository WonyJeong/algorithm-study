import sys

input = sys.stdin.readline


def stairNumber(N):
    memo = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(1, N):
        temp = [0 for _ in range(10)]
        for j in range(0, 10):
            if 0 < j < 9:
                temp[j - 1] += memo[j]
                temp[j + 1] += memo[j]
            elif j == 0:
                temp[j + 1] += memo[j]
            else:
                temp[j - 1] += memo[j]
        memo = temp

    print(sum(memo) % 1000000000)


if __name__ == "__main__":
    N = int(input().strip())
    stairNumber(N)
