import sys

input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def fishMove(x,y,arr,fish):

    for fishNumber, i, j in fish:
        dir_ = arr[i][j][1] - 1
        while True:
            ni = i + di[dir_]
            nj = j + dj[dir_]

            if ([ni,nj] != [x,y]) and 0 <= ni < 4 and 0 <= nj < 4:
                


def solution(arr, fish):
    fish = sorted(fish, key=lambda x: (x[0]))
    x = 0
    y = 0
    print(arr)  # 물고기번호, 방향
    print(fish)  # 물고기번호, i,j

    while True:
        fishNumber, direction = arr[x][y]
        arr[x][y] = [0, 0]
        del fish[fish.index([fishNumber, x, y])]
        arr = fishMove(x,y,arr, fish)



if __name__ == "__main__":
    arr = []
    fish = []
    for i in range(4):
        row = list(map(int, input().strip().split()))
        temp = []
        for j in range(0, 8, 2):
            temp.append([row[j], row[j + 1]])
            fish.append([row[j], i, j])
        arr.append(temp)

    solution(arr, fish)
