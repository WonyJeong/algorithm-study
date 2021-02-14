#10872
import sys
input = sys.stdin.readline

N = int(input().strip())

def factorial(n):
    if n <= 1 :
        return 1
    else :
        return n*factorial(n-1)

print(factorial(N))
