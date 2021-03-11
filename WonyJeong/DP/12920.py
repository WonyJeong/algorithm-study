import sys

input = sys.stdin.readline


# def solution(N, T):
#     print()
#     dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
#     for i in range(1, N + 1):
#         weight, score, limit = map(int, input().strip().split())
#         count = 0
#         for j in range(T + 1):
#             if weight <= j:
#                 temp = j // weight
#                 temp = min(temp, limit)
#                 dp[i][j] = max(score * temp, dp[i - 1][j])
#                 while temp > -1:
#                     dp[i][j] = max(
#                         dp[i][j],
#                         score * temp + dp[i - 1][j - weight * temp]
#                     )
#                     temp -= 1
#             else:
#                 dp[i][j] = dp[i - 1][j]

#         for d in dp:
#             print(d)
#         print("-------------------------------------")
#     print(dp[N][T])


def solution(N, T):
    dp = [0 for _ in range(T + 1)]
    for i in range(N):
        weight, score, limit = map(int, input().strip().split())
        bit = 1
        temp = 0
        while limit > 0:
            temp = min(limit,bit)
            for j in range(T, temp * weight - 1, -1):
                dp[j] = max(dp[j], score * temp + dp[j - weight * temp])
            bit *= 2∫
            limit -= temp

    print(dp[-1])


if __name__ == "__main__":
    N, T = map(int, input().strip().split())
    solution(N, T)
