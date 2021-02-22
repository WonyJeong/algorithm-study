import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))

    T = int(input().strip())
    for _ in range(T):
        axis, idx = map(int, input().strip().split())
        if axis == 1:
            for i in range(N):
                arr[i][idx - 1] += 1
        else:
            for j in range(M):
                arr[idx - 1][j] += 1

    for i in range(N):
        for j in range(M):
            if j == M - 1:
                print(arr[i][j] % 2)
            else:
                print(arr[i][j] % 2, end=" ")
