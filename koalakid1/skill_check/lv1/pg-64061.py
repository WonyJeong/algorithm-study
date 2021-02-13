def solution(board, moves):
    length = len(board[0])
    result = []
    count = 0
    for move in moves:
        for i in range(length):
            if board[i][move-1] != 0:
                next = board[i][move-1]
                board[i][move-1] = 0
                if result != [] and result[-1] == next:
                    del result[-1]
                    count += 2
                else:
                    result.append(next)
                break
    return count
