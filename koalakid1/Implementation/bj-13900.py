import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    integer = list(map(int,input().strip().split()))
    result = 0
    s = sum(integer)
    for i in range(N-1):
        s -= integer[i]
        result += integer[i] * s
    print(result)
