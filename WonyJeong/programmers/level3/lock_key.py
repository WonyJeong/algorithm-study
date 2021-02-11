import sys
import copy

input = sys.stdin.readline


def rotationKey(key):
    newKey = [[0 for _ in range(nk)] for _ in range(nk)]
    for i in range(nk):
        for j in range(nk):
            newKey[j][nk - i - 1] = key[i][j]
    return newKey


def compare(i, j):
    print(i, j)
    temp = [[0 for _ in range(nl + nk * 2)] for _ in range(nl + nk * 2)]

    for a in range(0, nl + nk * 2):
        for b in range(0, nl + nk * 2):
            temp[a][b] = lock_[a][b]

    for x in range(i, nk + i):
        for y in range(j, nk + j):
            temp[x][y] += key_[x - i][y - j]

    temp2 = [row[nk : nk + nl] for row in temp[nk : nk + nl]]

    if temp2 == comp:
        return 1

    return 0


def solution(key, lock):
    global nl, nk, key_, lock_, comp
    nk = len(key[0])
    nl = len(lock[0])

    comp = [[1 for _ in range(nl)] for _ in range(nl)]
    lock_ = [[0 for _ in range(nl + nk * 2)] for _ in range(nl + nk * 2)]

    for i in range(0, nl):
        for j in range(0, nl):
            lock_[i + nk][j + nk] = lock[i][j]

    key_ = key
    for k in range(0, 4):
        key_ = rotationKey(key_)
        for i in range(0, nk + nl + 1):
            for j in range(0, nk + nl + 1):
                answer = compare(i, j)
                if answer == 1:
                    return True

    return False


if __name__ == "__main__":
    # print(
    #     solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    # )

    print(solution([[0, 0], [0, 1]], [[1, 0], [1, 1]]))
