import sys

input = sys.stdin.readline


def fibonacci(n, memo):
    if n <= len(memo) - 1:
        print(" ".join(map(str, memo[n])))
        return

    for i in range(len(memo), n + 1):
        f11 = memo[i - 2][0]
        f12 = memo[i - 2][1]
        f21 = memo[i - 1][0]
        f22 = memo[i - 1][1]
        memo.append([f11 + f21, f12 + f22])

    print(" ".join(map(str, memo[n])))


if __name__ == "__main__":
    T = int(input().strip())
    memo = [[1, 0], [0, 1]]
    for _ in range(T):
        fibonacci(int(input().strip()), memo)