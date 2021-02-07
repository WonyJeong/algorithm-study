import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().strip().split())
        if m > n-m:
            m = n-m
        print(1 + (n - m) * m)
