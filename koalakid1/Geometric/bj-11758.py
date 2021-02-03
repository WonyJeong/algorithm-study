import sys


def CCW(A, B, C):
    temp = 0
    temp += A[0]*B[1]+B[0]*C[1]+C[0]*A[1]
    temp -= A[1]*B[0]+B[1]*C[0]+C[1]*A[0]
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    print(CCW(A, B, C))
