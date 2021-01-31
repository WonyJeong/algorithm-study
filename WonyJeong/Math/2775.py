import sys

input = sys.stdin.readline

# 1,3
def getNum(m, n):
    arr = []
    temp = []
    for i in range(1, n + 1):
        temp.append(i)
    arr.append(temp)

    for i in range(1, m + 1):
        temp = []
        val = 0
        for j in range(0, n):
            val += arr[i - 1][j]
            temp.append(val)
        arr.append(temp)

    print(arr[m][n - 1])
    # print(arr)


if __name__ == "__main__":
    answer = 0
    T = int(input().strip())
    for _ in range(0, T):
        i = int(input().strip())
        j = int(input().strip())
        getNum(i, j)
