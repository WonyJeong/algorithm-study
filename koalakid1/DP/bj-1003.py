import sys

input = sys.stdin.readline


def fibo(n):
    if n <= 1:
        return zero[n], one[n]
    if zero[n] != 0 or one[n]:
        return zero[n], one[n]
    zero[n] = fibo(n-1)[0] + fibo(n-2)[0]
    one[n] = fibo(n-1)[1] + fibo(n-2)[1]
    return zero[n], one[n]


T = int(input())

for _ in range(T):
    N = int(input())
    zero = [0 for _ in range(N+1)]
    one = [0 for _ in range(N+2)]
    zero[0] = 1
    one[1] = 1

    x, y = fibo(N)
    print(x, y)
