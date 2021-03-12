#4948
import sys
import math
input = sys.stdin.readline

def solution(N):
    isPrime = [False,False] + [True] * (N * 2 - 1)
    
    for i in range(2, 2*N+1):
        if isPrime[i]:
            for j in range(2*i, 2*N+1, i):
                isPrime[j] = False

    count = 0
    for i in range(N+1, 2*N+1):
        if isPrime[i]:
            #print(i)
            count += 1


    return count

if __name__ == '__main__':
    while True:
        N = int(input().strip())
        if N == 0 :
            break
        else :
            print(solution(N))