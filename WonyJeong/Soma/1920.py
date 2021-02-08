import sys

input = sys.stdin.readline


def findNumber(arr1, x):
    length = len(arr1)
    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2
        if arr1[mid] == x:
            print(1)
            return
        elif arr1[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    print(0)


if __name__ == "__main__":
    T1 = int(input().strip())
    arr1 = list(map(int, input().strip().split()))
    T2 = int(input().strip())
    arr2 = list(map(int, input().strip().split()))

    arr1 = sorted(arr1)

    for i in range(0, T2):
        findNumber(arr1, arr2[i])
