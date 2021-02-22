import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = [input().strip() for _ in range(4)]
    k = int(input())
    for _ in range(k):
        a,b = map(int,input().strip().split())
        
    result = 0
    for i in range(4):
        if t[i][0] == "1":
            result += 2 ** i
    print(result)