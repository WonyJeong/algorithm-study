#11729
import sys
input = sys.stdin.readline

N = int(input().strip())

def Hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        Hanoi(N - 1, a, c, b)
        print(a, c)
        Hanoi(N - 1, b, a, c)

k = 1
for i in range(N - 1):
    k = 2 * k + 1
print(k)
Hanoi(N, 1, 2, 3)