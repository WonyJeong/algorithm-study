import sys

input = sys.stdin.readline


def axisSorting(arr):
    for val in sorted(arr, key=lambda x: (x[0], x[1])):
        print(f"{val[0]} {val[1]}")


if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(0, T):
        temp = list(map(int, input().strip().split()))
        arr.append(temp)

    axisSorting(arr)