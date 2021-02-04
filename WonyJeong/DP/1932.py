import sys

input = sys.stdin.readline


def findMaximumValue(T):
    top = int(input().strip())
    arr = [top]
    for i in range(1, T):
        row = list(map(int, input().strip().split()))
        temp = []
        for j in range(0, len(row)):
            if j == 0:
                temp.append(arr[0] + row[0])
            else:
                if 0 < j < len(row) - 1:
                    comp = [row[j] + arr[j - 1], row[j] + arr[j]]
                    temp.append(max(comp))
                else:
                    temp.append(arr[j - 1] + row[j])
        arr = temp
    print(max(arr))


if __name__ == "__main__":
    T = int(input().strip())
    findMaximumValue(T)
