import sys

input = sys.stdin.readline


def solution(arr1, arr2):
    arr1Len = len(arr1)
    arr2Len = len(arr2)
    memo = []
    first = False
    for i in range(arr2Len):
        temp = [0]
        for j in range(arr1Len):
            if i == 0:
                if first == True:
                    temp.append(1)
                else:
                    if arr1[j] == arr2[i]:
                        temp.append(1)
                        first = True
                    else:
                        temp.append(0)
            else:
                if arr1[j] == arr2[i]:
                    temp.append(memo[j] + 1)
                else:
                    temp.append(max(memo[j + 1], temp[j]))
        memo = temp
    print(max(memo))


if __name__ == "__main__":
    N = int(input().strip())
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    solution(arr1, arr2)
