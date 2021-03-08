import sys

input = sys.stdin.readline


def solution(n):
    arr = [0, 1, 1]
    for i in range(3, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]


if __name__ == "__main__":
    print(solution(int(input().strip())))