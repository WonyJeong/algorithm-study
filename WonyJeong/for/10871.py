import sys
input = sys.stdin.readline

def listFilter(x,y):
    return x < y

N ,M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
result = [x for x in arr if listFilter(x,M)]
for x in result:
    print(x, end=" ")