#10814
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    arr = [ ['0']*2 for _ in range(N)]
    for i in range(N):
        arr[i][0], arr[i][1] = (input().strip().split())
    
    arr = sorted(arr, key=lambda x:(int(x[0])))
    for i in range(N):
        print(arr[i][0], arr[i][1])