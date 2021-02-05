import sys

input = sys.stdin.readline

# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않음
# 2 : 이번 포도주를 먹고 이전 포도주도 먹음
# 3 : 이번 포도주를 먹지 않음


def drinkWine(N):
    wine = [int(input().strip()) for x in range(N)]
    memo = [0]
    memo.append(wine[0])
    if N > 1:
        memo.append(wine[0] + wine[1])

    for i in range(3, N + 1):
        case_1 = wine[i - 1] + memo[i - 2]
        case_2 = wine[i - 1] + wine[i - 2] + memo[i - 3]
        case_3 = memo[i - 1]

        memo.append(max(case_1, case_2, case_3))

    print(memo[N])


if __name__ == "__main__":
    N = int(input().strip())
    drinkWine(N)
