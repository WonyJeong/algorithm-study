import sys

input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = input().strip()
        length = len(N)
        if int(N[0]) >= 5:
            result = int("5" + "0" * (length - 1)) * \
                int("4" + "9" * (length - 1))
        else:
            result = int(N) * (int("9" * length)-int(N))
        print(result)
