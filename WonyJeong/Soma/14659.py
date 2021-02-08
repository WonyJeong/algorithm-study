import sys

input = sys.stdin.readline


def hanjo(T, arr):
    max = 0
    i = 0
    while i < T - 1:
        if arr[i] > arr[i + 1]:
            x = arr[i]
            temp = 0
            j = i + 1
            while j < T:
                if arr[j] < x:
                    temp += 1
                    if temp > max:
                        max = temp
                else:
                    break
                j += 1
            i = j
        else:
            i += 1

    print(max)


if __name__ == "__main__":
    T = int(input().strip())
    arr = list(map(int, input().strip().split()))
    hanjo(T, arr)
