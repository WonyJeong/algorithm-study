import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = list()
for i in range(N):
    board.append(input().strip())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        for k in range(i, i+8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
        repair.append(first_W)

minVal = 9999
for i in repair:
    minVal = min(minVal, i, 64-i)
print(minVal)
