import sys
input = sys.stdin.readline

while True:
    x,y = map(int, input().strip().split())
    if x == 0 and y ==0 :
        break
    print(x+y)