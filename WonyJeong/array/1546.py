import sys

input = sys.stdin.readline


N = int(input().strip())
grades = list(map(float, input().strip().split()))

maxGrade = max(grades)

for i in range(0, N):
    grades[i] = grades[i] * 100 / maxGrade

print(sum(grades) / N)