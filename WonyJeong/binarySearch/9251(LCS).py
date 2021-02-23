import sys

input = sys.stdin.readline


def solution(string, input_):
    stringLen = len(string)
    inputLen = len(input_)

    arr = [[0 for _ in range(stringLen + 1)] for _ in range(inputLen + 1)]
    first = False
    for i in range(inputLen):
        for j in range(stringLen):
            if i == 0:
                if first == True:
                    arr[i + 1][j + 1] = 1
                else:
                    if string[j] == input_[i]:
                        arr[i + 1][j + 1] = 1
                        first = True
                    else:
                        arr[i + 1][j + 1] = 0
            else:
                if string[j] == input_[i]:
                    arr[i + 1][j + 1] = arr[i][j] + 1
                else:
                    arr[i + 1][j + 1] = max(arr[i][j + 1], arr[i + 1][j])

    print(max(arr[inputLen]))


if __name__ == "__main__":
    string = input().strip()
    inp = input().strip()
    solution(string, inp)
