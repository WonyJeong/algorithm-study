#1546
import sys
input = sys.stdin.readline
N = int(input().strip())
scores = list(map(int, input().strip().split()))
M = max(scores)
for i in range(0, N) :
    scores[i] = scores[i]/M*100
print(sum(scores)/N)
