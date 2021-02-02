import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    item = list(map(str, input().strip().split()))
    action = item[0]
    if action == "push":
        stack.append(item[1])
    if action == "pop":
        print(len(stack) == 0 and -1 or stack.pop())
    if action == "size":
        print(len(stack))
    if action == "empty":

        print(len(stack) == 0 and 1 or 0)
    if action == "top":
        print(len(stack) == 0 and -1 or stack[-1])
