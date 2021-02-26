import sys

input = sys.stdin.readline

def find(target):
    global parent
    if target == parent[target]:
        return target
    x = find(parent[target])
    parent[target] = x
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    parent = [i for i in range(n+1)]
    for _ in range(m):
        s,a,b = map(int,input().strip().split())
        if s == 0:
            union(a,b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")