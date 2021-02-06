import sys

input = sys.stdin.readline


def matrix(N, M):
    visitedRow = [False for _ in range(N + 1)]
    visitedCol = [False for _ in range(N + 1)]

    deletedRowLength = 0
    deletedRowCumSum = 0
    deletedColLength = 0
    deletedColCumSum = 0

    for _ in range(M):
        direction, idx = list(map(str, input().strip().split()))
        idx = int(idx)
        cum = 0
        if direction == "R":
            if visitedRow[idx] == True:
                print(0)
            else:
                removedColindexSum = deletedColCumSum + deletedColLength * idx
                rowSum = (idx + 1 + idx + N) * N // 2
                visitedRow[idx] = True
                deletedRowCumSum += idx
                deletedRowLength += 1
                print(rowSum - removedColindexSum)

        else:
            if visitedCol[idx] == True:
                print(0)
            else:
                removedRowindexSum = deletedRowCumSum + deletedRowLength * idx
                colSum = (idx + 1 + idx + N) * N // 2
                visitedCol[idx] = True
                deletedColCumSum += idx
                deletedColLength += 1
                print(colSum - removedRowindexSum)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    matrix(N, M)
