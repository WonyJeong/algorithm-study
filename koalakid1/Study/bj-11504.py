import sys

input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        X = int(input().strip().replace(" ", ""))
        Y = int(input().strip().replace(" ", ""))
        roulette = input().strip().replace(" ", "")
        count = 0
        for i in range(N):
            if i >= N-M+1:
                val = int(roulette[i:] + roulette[:(i+M) % N])
            else:
                val = int(roulette[i:i+M])
            if X <= val <= Y:
                count += 1
        print(count)
