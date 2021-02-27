import sys
input = sys.stdin.readline
from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다


def solution(N, A):
    dp = []
    for i in A:
        k = bisect_left(dp, i) #자신이 들어갈 위치 k
        if len(dp) <= k: #i가 가장 큰 숫자라면
            dp.append(i)
        else:
            dp[k] = i #자신보다 큰 수 중 최솟값과 대체
    return len(dp)


if __name__ == '__main__':
    N = input().strip()
    A = list(map(int, input().split()))
    print(solution(N,A))
