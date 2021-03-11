#1929
import sys
import math
input = sys.stdin.readline

def solution(element):
    if element == 1 :
        return False
    for i in range(2, int(math.sqrt(element))+1):
        if element % i == 0:
            return False
    return True


if __name__ == '__main__':
    M, N= map(int,input().strip().split())
    for element in range(M, N+1):
        if solution(element):
            print(element)
