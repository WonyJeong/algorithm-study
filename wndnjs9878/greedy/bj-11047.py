#11047
import sys
input = sys.stdin.readline

def numberOfCoins(A, K):
    num = 0
    for i in range(N-1,-1,-1): #시작값, 끝값(포함안됨), 증가값
        if K == 0 :
            break
        if A[i] > K :
            continue
        num += K // A[i]
        K %= A[i]
    return num

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    A = [int(input().strip()) for _ in range(N)]
    
    print(numberOfCoins(A,K))