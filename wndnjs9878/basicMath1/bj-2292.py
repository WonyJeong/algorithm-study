#2292
import sys
input  = sys.stdin.readline

def solved(N) :
    sumOfComb = 1
    comb = 0
    while True :
        sumOfComb += 6 * comb
        if N <= sumOfComb :
            break
        comb += 1
    return comb+1

if __name__ == '__main__' :
    N = int(input().strip())
    print(solved(N))