import sys
from collections import deque 
input = sys.stdin.readline
        

if __name__ == "__main__":
    while True:
        a,b,c = map(int,input().strip().split())
        if a == b == c == 0:
            break
        a1 = 1
        b1 = 1
        if c >= 2:
            a2 = 1
            b2 = 2
            for i in range(2,c):
                a1,a2 = a2,a1+a2
                b1,b2 = b2,b1+b2
                print(a1,a2,b1,b2)
            a1 = a2
            b1 = b2
        print(a * a1 + b * b1)