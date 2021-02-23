#2502
import sys
input = sys.stdin.readline

def fibo(D):
    '''
    A : fibonacci[D-3]
    B : fibonacci[D-2]
    '''
    temp = [i for i in range(D)]
    temp[0] = 1
    temp[1] = 1
    for i in range(2,D):
        temp[i] = temp[i-1] + temp[i-2]
    A = temp[D-3]
    B = temp[D-2]
    AandB = [A,B]
    return AandB

def solution(D, K):
    frontA, frontB = fibo(D)
    A = 1
    forB = (K - frontA*A) % frontB
    while forB != 0 :
        A += 1
        forB = (K - frontA*A) % frontB
    B = (K - frontA*A) // frontB
    result = [A, B]
    return result
    
if __name__ == '__main__':
    D, K = map(int, input().strip().split())
    for element in solution(D,K):
        print(element)