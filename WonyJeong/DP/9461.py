import sys

input = sys.stdin.readline


def waveSequence(N):
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, N + 1):
        arr.append(arr[i - 1] + arr[i - 5])

    print(arr[N])


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        waveSequence(int(input().strip()))
