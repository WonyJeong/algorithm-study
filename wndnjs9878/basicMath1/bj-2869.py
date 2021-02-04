#2869
import sys
import math
input = sys.stdin.readline

def solved(A, B, V):
    return math.ceil((V-A)/(A-B)) + 1
         
if __name__ == '__main__':
    A, B, V = map(int, input().strip().split())
    print(solved(A,B,V))