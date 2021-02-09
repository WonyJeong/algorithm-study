import sys

input = sys.stdin.readline


def solution(m, n, puddles):
    history = [[0 for _ in range(m)] for _ in range(n)]

    for i, j in puddles:
        history[j - 1][i - 1] = -1

    flag = False
    print(history)
    for i in range(0, m):
        if history[0][i] == 0 and flag == False:
            history[0][i] = 1
        else:
            flag = True
            history[0][i] = -1
    flag = False
    for i in range(0, n):
        if history[i][0] != -1 and flag == False:
            history[i][0] = 1
        else:
            flag = True
            history[i][0] = -1

    print(history)

    for i in range(1, n):
        for j in range(1, m):
            if history[i][j] != -1:
                up = history[i - 1][j]
                left = history[i][j - 1]

                if up != -1 and left != -1:
                    history[i][j] = up + left
                elif up == -1 and left == -1:
                    history[i][j] = 0
                elif up == -1:
                    history[i][j] = left
                elif left == -1:
                    history[i][j] = up
            else:
                history[i][j] = -1
    return history[n - 1][m - 1] % 1000000007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
    # print(solution(10, 2, [[1, 2], [2, 3]]))
