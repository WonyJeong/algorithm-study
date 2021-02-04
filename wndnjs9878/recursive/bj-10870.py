#10870
import sys
input = sys.stdin.readline

def solved(n):
    if n == 0 or n == 1 :
        return n
    return solved(n-1)+solved(n-2)

if __name__ == '__main__':
    n = int(input().strip())
    print(solved(n))