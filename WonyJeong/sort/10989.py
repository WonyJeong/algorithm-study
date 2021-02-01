# 10,000,000

import sys

input = sys.stdin.readline


def countingSort(T, ct):
    flag = 0
    for i in range(0, 10001):
        if flag == T:
            break

        if ct[i] > 0:
            for j in range(0, ct[i]):
                print(i)
            flag += 1


if __name__ == "__main__":
    ct = [0 for _ in range(0, 10002)]
    T = int(input().strip())
    for _ in range(0, T):
        temp = int(input().strip())
        ct[temp] += 1

    countingSort(T, ct)
