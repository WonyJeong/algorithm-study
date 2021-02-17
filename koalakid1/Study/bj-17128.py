import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    Q = list(map(int, input().strip().split()))
    times = [0 for _ in range(n)]
    for i in range(n):
        times[i] = A[i] * A[(i+1) % n] * A[(i+2) % n] * A[(i+3) % n]
    s = sum(times)
    for i in Q:
        for j in range(i-4, i):
            j %= n
            times[j] = -times[j]
            s += 2 * times[j]
        print(s)
