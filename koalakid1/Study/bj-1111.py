import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().strip().split()))
    if N == 1:
        print("A")
    elif N == 2:
        if arr[0] == arr[1]:
            print(arr[0])
        else:
            print("A")
    else:
        if arr[1] - arr[0] == 0:
            a = 0
            b = arr[1]
        else:
            a = (arr[2] - arr[1]) // (arr[1] - arr[0])
            b = arr[1] - arr[0] * a

        result = True
        for i in range(2, N):
            if arr[i] != arr[i-1] * a + b:
                result = False
                break

        if result:
            print(arr[N-1] * a + b)
        else:
            print("B")
