import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        delay = list(map(int, input().strip().split()))
        dp = {}
        for i in range(1, N+1):
            dp[i] = set()
        for _ in range(K):
            start, end = map(int, input().strip().split())
            dp[end].add(start)

        W = int(input())
        done = set()
        wholeTime = 0
        doneW = True
        while doneW:
            build = []
            for i in dp:
                if done.issuperset(dp[i]) and i not in done:
                    build.append(i)

            time = min([delay[i-1] for i in build])
            wholeTime += time

            for b in build:
                delay[b-1] -= time
                if delay[b-1] == 0:
                    done.add(b)
                    if b == W:
                        doneW = False
        print(wholeTime)
