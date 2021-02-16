#2676
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T) :
        n, m = map(int, input().strip().split())
        print(m * (n - m) + 1)

