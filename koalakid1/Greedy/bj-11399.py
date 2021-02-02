import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int, input().strip().split()))
times = sorted(times)

results = []
for time in range(N):
    result = 0
    if time == 0:
        result += times[time]
    else:
        result += times[time] + results[time-1]
    results.append(result)

print(sum(results))
