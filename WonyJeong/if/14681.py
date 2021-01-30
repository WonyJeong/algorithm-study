import sys
input = sys.stdin.readline

x = int(input().strip())
y = int(input().strip())

if x*y > 0:
    if x >0 :
        print(1)
    else:
        print(3)
else:
    if x > 0:
        print(4)
    else :
        print(2)
