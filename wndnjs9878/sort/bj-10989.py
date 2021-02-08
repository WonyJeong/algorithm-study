#10989
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    arr = [0] * 10001
    for _ in range(N):
        arr[int(input().strip())] += 1
    for i in range(10001):
        if arr[i] != 0 :
            for _ in range(arr[i]):
                print(i)
    