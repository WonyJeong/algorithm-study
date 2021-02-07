#1018
import sys
input = sys.stdin.readline

def solution(N,M,board) :
    blackBoard = [
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B']
    ]
    whiteBoard = [
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W']
    ]
    result = 64
    for i in range(N-7):
        for j in range(M-7):
            blackBoardneedChange = 0
            whiteBoardneedChange = 0
            for k in range(0,8):
                for l in range(0,8):
                    if board[i+k][j+l] != blackBoard[k][l]:
                        blackBoardneedChange += 1
                    if board[i+k][j+l] != whiteBoard[k][l]:
                        whiteBoardneedChange += 1
            result = min(result,blackBoardneedChange,whiteBoardneedChange)
    return result


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    board = [list(input().strip()) for _ in range(N)]
    print(solution(N,M,board))
        