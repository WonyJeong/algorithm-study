import sys

input = sys.stdin.readline


def solution(n):
    arr = [0, 1, 2, 4]
    for i in range(4, n + 1):
        arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

    return arr[n]


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        print(solution(int(input().strip())))