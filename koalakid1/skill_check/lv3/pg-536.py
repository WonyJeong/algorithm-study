def solution(dirs):
    length = len(dirs)
    visited = [["" for _ in range(11)] for _ in range(11)]
    x = 5
    y = 5
    count = 0
    for index in dirs:
        if index == "U":
            n_x = x
            n_y = y+1
            if 0 <= n_x <= 10 and 0 <= n_y <= 10 and "U" not in visited[n_x][n_y] and "D" not in visited[x][y]:
                count += 1
                visited[n_x][n_y] += index

        elif index == "D":
            n_x = x
            n_y = y-1
            if 0 <= n_x <= 10 and 0 <= n_y <= 10 and "D" not in visited[n_x][n_y] and "U" not in visited[x][y]:
                count += 1
                visited[n_x][n_y] += index

        elif index == "R":
            n_x = x+1
            n_y = y
            if 0 <= n_x <= 10 and 0 <= n_y <= 10 and "R" not in visited[n_x][n_y] and "L" not in visited[x][y]:
                count += 1
                visited[n_x][n_y] += index

        else:
            n_x = x-1
            n_y = y
            if 0 <= n_x <= 10 and 0 <= n_y <= 10 and "L" not in visited[n_x][n_y] and "R" not in visited[x][y]:
                count += 1
                visited[n_x][n_y] += index

        if 0 <= n_x <= 10 and 0 <= n_y <= 10:
            print(x, y, n_x, n_y, count, visited[x][y], visited[n_x][n_y])
            x = n_x
            y = n_y

    return count
