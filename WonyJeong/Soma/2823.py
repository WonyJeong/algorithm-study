import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    H, W = map(int, input().strip().split())
    map_ = []
    comAnswer = 0
    for _ in range(H):
        row = list(input().strip())
        map_.append(row)

    for i in range(0, H):
        for j in range(0, W):
            temp = 0
            if map_[i][j] == ".":
                for k in range(0, 4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < H and 0 <= ny < W and map_[nx][ny] == ".":
                        temp += 1
                if temp < 2:
                    print(1)
                    exit(0)
    print(0)
