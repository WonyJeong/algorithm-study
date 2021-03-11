#4948
import sys
import math
input = sys.stdin.readline

def solution(N):
    answer = 0
    for element in range(N, 2*N+1):
        if element == 1 :
            continue
        else:
            for i in range(2, int(math.sqrt(element))+1):
                if element % i == 0:
                    break
                elif i == int(math.sqrt(element)):
                    answer += 1
                
    return answer

if __name__ == '__main__':
    while True:
        N = int(input().strip())
        if N == 0 :
            break
        else :
            print(solution(N))