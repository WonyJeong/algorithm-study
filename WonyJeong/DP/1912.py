import sys

input = sys.stdin.readline


def solution(T, arr):
    memo = [arr[0]]
    max_ = arr[0]
    for i in range(1, T):
        temp = memo[i - 1] + arr[i]
        memo.append(temp if temp > 0 else 0)
        if max_ < 0 and arr[i] > max_:
            max_ = arr[i]
        elif memo[i] != 0 and memo[i] > max_:
            max_ = memo[i]
    print(max_)


if __name__ == "__main__":
    T = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(T, arr)
