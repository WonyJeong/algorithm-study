#1712
import sys
input = sys.stdin.readline
def breakEvenPoint(A,B,C):
    if (C-B) > 0 :
        point = A / (C-B)
        print(int(point+1))
    else :
        print(-1)

if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    breakEvenPoint(A,B,C)