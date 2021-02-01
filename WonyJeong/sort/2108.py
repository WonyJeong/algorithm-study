import sys

input = sys.stdin.readline


def printCenterValue(T, arr):
    cursor = 0
    for i in range(0, 8001):
        if arr[i] != 0:
            cursor += arr[i]
            if cursor > T // 2:
                print(i - 4000)
                break


def printMostfrequent(T, _max, arr):
    firstValue = max(arr)
    firstIndex = arr.index(firstValue)

    del arr[firstIndex]

    secondValue = max(arr)
    secondIndex = arr.index(secondValue) + 1

    if firstValue > secondValue:
        print(firstIndex - 4000)
    else:
        print(secondIndex - 4000)

    # arr.count(max)


if __name__ == "__main__":
    arr = [0 for _ in range(0, 8001)]
    T = int(input().strip())

    temp = int(input().strip())
    _min = temp
    _max = temp
    arr[temp + 4000] += 1
    sum = temp
    for i in range(1, T):
        temp = int(input().strip())
        arr[temp + 4000] += 1
        if _min > temp:
            _min = temp
        if _max < temp:
            _max = temp
        sum += int(temp)

    print(round(sum / T))
    printCenterValue(T, arr)
    printMostfrequent(T, _max, arr)
    print(_max - _min)