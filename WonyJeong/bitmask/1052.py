import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    z = n
    while bin(n).count("1") > k:
        n += n & -n
        print(n - z)
