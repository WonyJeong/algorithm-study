import sys

input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(0, T):
        temp = int(input().strip())
        arr.append(temp)

    for val in sorted(arr, reverse=True):
        print(val)
