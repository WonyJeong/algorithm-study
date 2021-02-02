#2675
import sys
input = sys.stdin.readline
def solved(repeat, string):
    for i in range(0,len(S)) :
        for j in range(0, R) :
            print(S[i], end='')
    print()

if __name__ == '__main__' :
    T = int(input().strip())
    for i in range(0,T) :
        R, S = input().strip().split()
        R = int(R)
        solved(R, S)