import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input().strip())
    arr = []
    for _ in range(T):
        n, m = map(int, input().strip().split())
        print(1 + (n - m) * m)
