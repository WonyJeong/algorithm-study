import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    f = list(map(int,input().strip().split()))
    
    a = sum(f) // 2
    b = f.pop(f.index(a))
    
    for i in f:
        print(i, end = " ")
    print(b)