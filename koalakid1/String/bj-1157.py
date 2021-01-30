import sys

input = sys.stdin.readline

string = input().strip().lower()
alphaCount = [0 for _ in range(26)]
for i in string:
    alphaCount[ord(i)-ord('a')] += 1

if alphaCount.count(max(alphaCount)) == 1:
    print(chr(alphaCount.index(max(alphaCount))+ord('A')))
else:
    print("?")
