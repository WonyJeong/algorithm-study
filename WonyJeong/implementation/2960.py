import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = [True for _ in range(N + 1)]
    ct = 0
    for i in range(2, N + 1):
        if arr[i] == True:
            for j in range(i, N + 1, i):
                if arr[j] == True:
                    ct += 1
                    arr[j] = False

                    if ct == M:
                        print(j)
