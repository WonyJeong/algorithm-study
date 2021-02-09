import sys

input = sys.stdin.readline


def iq(N, arr):
    if N > 2:
        a0 = arr[0]
        a1 = arr[1]
        a2 = arr[2]

        if a1 == a0:
            x = 0
        else:
            x = (a2 - a1) // (a1 - a0)

        y = a1 - a0 * x

        for i in range(0, N - 1):
            if arr[i] * x + y != arr[i + 1]:
                print("B")
                return

        print(arr[N - 1] * x + y)

    elif N == 1:
        print("A")
    elif N == 2:
        if arr[0] == arr[1]:
            print(arr[0])
        else:
            print("A")


if __name__ == "__main__":
    N = int(input().strip())
    iq(N, list(map(int, input().strip().split())))
