import sys

input = sys.stdin.readline


def cowcowcow(N, Q, cows, q):
    k = []
    sum_ = 0
    oper = [1 for _ in range(N)]
    for i in range(0, N - 4):
        temp = cows[i] * cows[i + 1] * cows[i + 2] * cows[i + 3]
        k.append(temp)
        sum_ += temp
    for i in range(N - 4, N):
        temp = cows[i % N] * cows[(i + 1) % N] * cows[(i + 2) % N] * cows[(i + 3) % N]
        k.append(temp)
        sum_ += temp

    for i in range(0, len(q)):
        q_ = q[i] - 1
        for j in range(0, 4):
            idx = (q_ + N - j) % N
            oper[idx] *= -1
            sum_ += k[idx] * 2 * oper[idx]
        print(sum_)


if __name__ == "__main__":
    N, Q = map(int, input().strip().split())
    cows = list(map(int, input().strip().split()))
    q = list(map(int, input().strip().split()))

    cowcowcow(N, Q, cows, q)
