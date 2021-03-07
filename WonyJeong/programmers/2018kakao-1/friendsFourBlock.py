import sys

input = sys.stdin.readline


def rematchBoard(board):
    temp = list(map(list, zip(*board)))
    for i in range(len(temp)):
        ct = 0
        while "X" in temp[i]:
            temp[i].remove("X")
            ct += 1

        for j in range(ct):
            temp[i].insert(0, "X")

    return list(map(list, zip(*temp)))


def blockMarking(blocks, board):
    for i, j in blocks:
        board[i][j] = "X"
    return rematchBoard(board)


def solution(m, n, board):
    answer = 0
    flag = True
    for i in range(m):
        board[i] = list(map(str, board[i]))

    while flag:
        flag = False
        removedBlock = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if (
                    board[i][j] != "X"
                    and board[i][j] == board[i][j + 1]
                    and board[i][j] == board[i + 1][j]
                    and board[i][j] == board[i + 1][j + 1]
                ):
                    flag = True
                    removedBlock.add(tuple([i, j]))
                    removedBlock.add(tuple([i, j + 1]))
                    removedBlock.add(tuple([i + 1, j]))
                    removedBlock.add(tuple([i + 1, j + 1]))

        if flag == True:
            answer += len(removedBlock)
            board = blockMarking(removedBlock, board)

    return answer


if __name__ == "__main__":
    print("1 : ", solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(
        "2 : ",
        solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]),
    )
    print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
