#2675
import sys

input = sys.stdin.readline
T = int(input().strip()) #테스트케이스 개수

for i in range(0,T):
    R, S = input().strip().split() #반복횟수 , 문자열
    R = int(R)
    P = ""
    for i in range(0, len(S)):
        P += R * S[i]
    print(P)