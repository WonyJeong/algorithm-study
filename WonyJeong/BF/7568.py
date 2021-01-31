import sys

input = sys.stdin.readline


def dungchi(N, arr):
    answer = []
    for i in range(0, N):
        answer.append(1)

    for i in range(0, N):
        w = arr[i][0]
        h = arr[i][1]
        for j in range(0, N):
            _w = arr[j][0]
            _h = arr[j][1]
            if i == j:
                continue
            else:
                if w > _w and h > _h:
                    answer[j] += 1

    for val in answer:
        print(val, end=" ")


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for i in range(0, N):
        temp = list(map(int, input().strip().split()))
        arr.append(temp)
    dungchi(N, arr)
