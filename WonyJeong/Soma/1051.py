import sys

input = sys.stdin.readline


def numberSquar(h, w, arr):
    maxWidth = h if h > w else w
    max = 1
    for i in range(1, maxWidth):
        for k in range(0, h - i):
            for j in range(0, w - i):
                if arr[k][j] == arr[k][j + i] == arr[k + i][j] == arr[k + i][j + i]:
                    max = (i + 1) * (i + 1)

    print(max)


if __name__ == "__main__":
    H, W = map(int, input().strip().split())
    arr = []
    for _ in range(H):
        temp = list(map(int, map(str, input().strip())))
        arr.append(temp)
    numberSquar(H, W, arr)
