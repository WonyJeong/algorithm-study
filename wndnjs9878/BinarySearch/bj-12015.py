#14003
import sys
from bisect import bisect_left
input = sys.stdin.readline


def solution(N, seq):
    lis = []

    for num in seq:
        idx = bisect_left(lis, num) #자신이 들어갈 위치 k
        if len(lis) <= idx: #num가 가장 큰 숫자라면
            lis.append(num)
        else:
            lis[idx] = num #자신보다 큰 수 중 최솟값과 대체

    print(len(lis))


if __name__ == "__main__":
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))
    solution(N, seq)