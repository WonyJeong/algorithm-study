import sys
input = sys.stdin.readline

a,b = map(int, input().strip().split())

if a > b :
    print(">")
elif a == b :
    print("==")
else:
    print("<")

    