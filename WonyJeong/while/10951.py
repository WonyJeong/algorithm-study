import sys
input = sys.stdin.readline

while True:
    try:
        x,y = map(int, input().strip().split())
        print(x+y)
    except:
        break