import sys

input = sys.stdin.readline

string = input().strip()
result = [-1 for _ in range(26)]
for i in range(len(string)):
    pos = ord(string[i]) - ord('a')
    if result[pos] == -1:
        result[pos] = i

print(" ".join(str(i) for i in result))
