import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input().strip()

    P = ""
    for _ in range(N):
        P += "IO"
    P += "I"
    lenP = len(P)
    count = 0
    print(S.count(P))
    for i in range(M - lenP + 1):
        if S[i:i+lenP] == P:
            count += 1
    print(count)
