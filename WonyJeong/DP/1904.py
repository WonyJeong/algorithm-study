import sys

input = sys.stdin.readline


def tile(n):
    arr = [0, 1, 2]

    if n < 3
        print(arr[n])

    for i in range(3, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % 15746)

    print(arr[n])


if __name__ == "__main__":
    tile(int(input().strip()))