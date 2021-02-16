import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input().strip()

    lenP = 2*N + 1
    count = 0
    answer = 0
    for i in range(M):
        if (count % 2 == 0 and S[i] == "I") or (count % 2 == 1 and S[i] == "O"):
            count += 1
        else:
            if count - lenP >= 0:
                answer += (count - lenP) // 2 + 1
            count = 0
            if S[i] == "I":
                count += 1
    if count - lenP >= 0:
        answer += (count - lenP) // 2 + 1
    print(answer)
