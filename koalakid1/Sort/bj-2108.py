import sys

input = sys.stdin.readline

N = int(input())

sumVal = 0
result = []
counter = [0] * 8001
for _ in range(N):
    data = int(input())
    result.append(data)
    sumVal += data
    counter[data+4000] += 1

result = sorted(result)

maxC = max(counter)
indexC = counter.index(maxC)
counter[indexC] = 0
secondC = max(counter)

print(f"{round(sumVal/N)}")
print(result[N//2])
if maxC > secondC:
    print(indexC-4000)
else:
    print(counter.index(maxC)-4000)
print(-result[0] + result[-1])
