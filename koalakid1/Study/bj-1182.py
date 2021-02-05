import sys
input = sys.stdin.readline


def subS(index, total):
    global count
    if index == N:
        return
    total += intList[index]
    if total == S:
        count += 1

    subS(index + 1, total)
    subS(index + 1, total - intList[index])


if __name__ == "__main__":
    N, S = map(int, input().strip().split())
    intList = list(map(int, input().strip().split()))
    count = 0
    subS(0, 0)
    print(count)
