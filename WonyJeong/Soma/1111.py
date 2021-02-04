import sys

input = sys.stdin.readline

# rule : (앞수*a) + b
# 어케푸냐
def iq(N, arr):
    diff = []

    for i in range(0, len(arr) - 1):
        x = arr[i + 1] // arr[i]
        y = arr[i + 1] % arr[i]
        print(x, y)

    print(diff)


if __name__ == "__main__":
    N = int(input().strip())
    iq(N, list(map(int, input().strip().split())))
