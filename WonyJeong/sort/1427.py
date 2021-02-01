import sys

input = sys.stdin.readline


def reverseSorting(str_):
    arr = []
    for char in str_:
        arr.append(int(char))

    list_ = sorted(arr, reverse=True)
    print("".join(map(str, list_)))


if __name__ == "__main__":
    str_ = input().strip()
    reverseSorting(str_)
