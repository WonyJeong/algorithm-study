#10870
import sys

input = sys.stdin.readline

N = int(input().strip())
print(fibonacci(N))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)