import sys

input = sys.stdin.readline


def axisSorting(arr):
    arr = sorted(sorted(arr), key=lambda x: len(x))
    for s in arr:
        print(s)


if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(0, T):
        temp = input().strip()
        if temp in arr:
            continue
        else:
            arr.append(temp)

    axisSorting(arr)
