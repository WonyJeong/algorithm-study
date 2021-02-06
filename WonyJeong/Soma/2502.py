import sys

input = sys.stdin.readline


def ricecake(N, K):
    fibo = [[1, 0], [0, 1]]
    for i in range(2, N):
        fibo.append([fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]])

    x, y = fibo[N - 1]

    for a in range(1, sys.maxsize):
        for b in range(a + 1, sys.maxsize):
            if a * x + y * b == K:
                print(a)
                print(b)
                exit(1)

            if a * x + y * b > K:
                break


if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    ricecake(N, K)
