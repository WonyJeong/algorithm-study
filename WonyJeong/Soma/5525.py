import sys

input = sys.stdin.readline

### 루프 조건 추가해야함


def IOIOIOIO(N, arr):
    ioi = ["I"] + ["O", "I"] * N
    oi = ["O", "I"]
    cursor = 0
    answer = 0
    i = 0
    j = 0
    while i < len(arr) - 2 * N:

        if arr[i] == "I":
            if ioi == arr[i : i + 2 * N + 1]:
                temp = 1
                j = i + 2 * N + 1
                while True:
                    if arr[j : j + 2] == oi:
                        temp += 1
                        j += 2
                    else:
                        break
                i = j
                answer += temp
            else:
                i += 1
        else:
            i += 1

    print(answer)


if __name__ == "__main__":
    N = int(input().strip())
    L = int(input().strip())
    IO = list(input().strip())

    IOIOIOIO(N, IO)
