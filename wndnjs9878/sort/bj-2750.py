#2750
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(int(input().strip()))
    arr.sort()
    for element in arr:
        print(element)
 