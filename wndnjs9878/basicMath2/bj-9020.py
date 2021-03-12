#9020 골드바흐의 추측 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
import sys
input = sys.stdin.readline

def solution(N):
    # 에라토스테네스의 체
    isPrime = [False,False] + [True] * (N-1)
    prime = []
    for i in range(2, N+1):
        if isPrime[i]:
            prime.append(i)
            for j in range(2*i, N+1, i):
                isPrime[j] = False

    # 두 소수의 차이가 가장 작은 것의 합으로 N 만들기 
    startIdx = max(i for i in range(len(prime)) if prime[i] <= N / 2)
    for i in range(startIdx, -1, -1):
        for j in range(i, len(prime)):
            if prime[i] + prime[j] == N :
                return [prime[i], prime[j]]

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(" ".join(map(str,solution(N))))