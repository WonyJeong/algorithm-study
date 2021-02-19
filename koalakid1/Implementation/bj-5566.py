import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    act = [int(input()) for _ in range(n)]
    dice = [int(input()) for _ in range(m)]
    index = 0
    for i in dice:
        index += i
        if index >= n-1:
            print(i+1)
            break
        index += act[index]
        if index >= n-1:
            print(i+1)
            break        