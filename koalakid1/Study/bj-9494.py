import sys

input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break

        strings = [input().strip() for _ in range(n)]

        index = 0
        for string in strings:
            next = string.find(" ", index)
            if next == -1:
                index = max(index, len(string))
            elif next != index:
                index = next
        print(index + 1)
