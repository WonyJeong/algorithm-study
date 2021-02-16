#1182
import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == '__main__' :
    N, S = map(int, input().strip().split())
    sequence = list(map(int, input().strip().split()))
    cnt = 0

    for i in range(1,N+1):
        comb = list(combinations(sequence,i))
        for j in range(len(comb)):
            partialSum = sum(comb[j])
            if partialSum == S :
                cnt += 1
    print(cnt)