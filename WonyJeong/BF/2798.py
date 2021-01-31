import sys

input = sys.stdin.readline


def blackjack(N, M, nums):
    answer = -1

    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (
                    answer < nums[i] + nums[j] + nums[k]
                    and M >= nums[i] + nums[j] + nums[k]
                ):
                    answer = nums[i] + nums[j] + nums[k]

    print(answer)


if __name__ == "__main__":
    answer = 0
    N, M = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    blackjack(N, M, nums)
