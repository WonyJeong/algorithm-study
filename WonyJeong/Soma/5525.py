import sys

input = sys.stdin.readline


def IOIOIOIO(N, arr):
    ioi = ["I"] + ["O", "I"] * N
    oi = ["O", "I"]
    cursor = 0
    answer = 0
    i = 0
    j = 0
    while i < len(arr) - 2 * N:
        if arr[i : i + 2] == ["I", "O"]:
            temp = 0
            while arr[i + 1 : i + 3] == oi:
                i += 2
                temp += 1
                if arr[i] == "I" and temp == N:
                    temp -= 1
                    answer += 1

        i += 1
    print(answer)


if __name__ == "__main__":
    N = int(input().strip())
    L = int(input().strip())
    IO = list(input().strip())

    IOIOIOIO(N, IO)
