import sys

input = sys.stdin.readline


def ageSorting(arr):
    for val in sorted(arr, key=lambda x: x[0]):
        print(f"{val[0]} {val[1]}")


if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(0, T):
        age, name = map(str, input().strip().split())
        age = int(age)
        arr.append([age, name])
    ageSorting(arr)
