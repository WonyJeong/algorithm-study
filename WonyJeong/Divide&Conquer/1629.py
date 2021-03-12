import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a, b, c = map(int, input().strip().split())
    print(pow(a, b, c))
