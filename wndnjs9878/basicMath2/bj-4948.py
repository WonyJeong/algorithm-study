#4948 에라토스테네스의 체 
import sys
input = sys.stdin.readline

def solution(N):
    # 에라토스테네스의 체
    isPrime = [False,False] + [True] * (N * 2 - 1)
    
    for i in range(2, 2*N+1):
        if isPrime[i]:
            # 소수 따로 저장하고 싶을때, 코드 작성하는 부분
            for j in range(2*i, 2*N+1, i):
                isPrime[j] = False

    # 주어진 범위에서 소수 개수 구하기 
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