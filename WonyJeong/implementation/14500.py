import sys

input = sys.stdin.readline


cases = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [1, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [0, 1], [1, 1], [-1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 1], [1, 0]],
]


def getScore(i, j):
    score = 0
    for block in cases:
        temp = 0
        for x, y in block:
            if 0 <= i + x < N and 0 <= j + y < M:
                temp += paper[i + x][j + y]
            else:
                break
        if score < temp:
            score = temp

    return score


def tetromino(N, M, paper):
    answer = 0

    for i in range(0, N):
        for j in range(0, M):
            temp = getScore(i, j)
            if answer < temp:
                answer = temp

    print(answer)


if __name__ == "__main__":
    global N, M, paper
    N, M = map(int, input().strip().split())
    paper = []
    for _ in range(N):
        temp = list(map(int, input().strip().split()))
        paper.append(temp)

    tetromino(N, M, paper)
