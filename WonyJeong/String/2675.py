import sys

input = sys.stdin.readline

N = int(input().strip())
for _ in range(0, N):
    R, word = map(str, input().strip().split())
    R = int(R)
    answer = ""
    for i in range(len(word)):
        answer += word[i] * R
    print(answer)
