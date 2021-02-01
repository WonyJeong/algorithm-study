import sys

input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(0, T):
        temp = int(input().strip())
        arr.append(temp)
    # 이건 왜 안댐?
    # arr = arr.sort()
    for val in sorted(arr):
        print(val)
