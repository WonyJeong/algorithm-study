import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    a, b, c = map(int, input().strip().split())
    print(pow(a, b, c))
