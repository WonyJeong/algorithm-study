from abc import abstractproperty
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    factor = list(map(int, input().strip().split()))
    print(max(factor)*min(factor))
