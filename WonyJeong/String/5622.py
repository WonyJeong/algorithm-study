import sys

input = sys.stdin.readline

words = input().strip().lower()

s = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

time = 0
for i in range(len(words)):
    for j in s:
        if words[i] in j:
            time += s.index(j) + 3
print(time)