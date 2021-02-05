import sys

input = sys.stdin.readline


def findArea(N, arr):
    answer = 0
    for i in range(N):
        temp = arr[i].split("X")
        for j in range(0, len(temp)):
            if len(temp[j]) >= 2:
                answer += 1

    return answer


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(input().strip())

    transpose = []

    for i in range(N):
        temp = ""
        for j in range(N):
            temp += arr[j][i]
        transpose.append(temp)

    print(findArea(N, arr), findArea(N, transpose))
