import sys

input = sys.stdin.readline


def easyMath(S, E):
    arr = []
    zeroToStart = 0

    i = 0
    j = 0
    ct = 0
    while True:
        i += 1
        j = 0
        while j < i:
            arr.append(i)
            j += 1
            ct += 1
            if ct < S:
                zeroToStart += i
            if ct == E:
                print(sum(arr) - zeroToStart)
                exit(0)


if __name__ == "__main__":
    S, E = map(int, input().strip().split())
    easyMath(S, E)
