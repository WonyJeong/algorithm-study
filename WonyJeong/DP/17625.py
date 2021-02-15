import sys


def fourSquares(N):
    answer = [4 for _ in range(N + 1)]
    for i in range(1, N + 1):
        sq = i ** 2
        if sq <= N:
            answer[sq] = 1
        else:
            break

    for i in range(2, N + 1):
        if not answer[i] == 1:
            for j in range(1, i):
                if j * j <= i:
                    answer[i] = min(answer[i], answer[i - j ** 2] + 1)
                else:
                    break

    print(answer[N])


if __name__ == "__main__":
    N = int(input().strip())
    fourSquares(N)
