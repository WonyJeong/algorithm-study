import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(n)
print(sum(stack))
