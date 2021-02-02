import sys
import operator
input = sys.stdin.readline

N = int(input())

times = []

for _ in range(N):
    times.append(list(map(int, input().strip().split())))

times = sorted(times, key=operator.itemgetter(0, 1))

start = -1
end = -1
count = 0
for s, e in times:
    if s >= end:
        count += 1
        start = s
        end = e
    elif e < end:
        end = e
print(count)
