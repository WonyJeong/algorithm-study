import sys

input = sys.stdin.readline
# 97 ~ 122
arr = []
for i in range(0, 26):
    arr.append(0)

_word = input().strip()

word = _word.lower()

for i in range(len(word)):
    arr[ord(word[i]) - 97] += 1

maxValue = max(arr)
ct = 0
for i in range(0, 26):
    if arr[i] == maxValue:
        ct += 1

print(ct == 1 and chr(arr.index(maxValue) + 65) or "?")
