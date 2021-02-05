import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B = map(int, input().strip().split())
    maxIndex = []
    count = 0
    length = 0
    while length <= B:
        count += 1
        maxIndex += [count] * count
        length += count
    print(sum(maxIndex[A-1:B]))
