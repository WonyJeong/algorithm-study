#1717
import sys
input = sys.stdin.readline
mm={}
def find_parent(x):
    if mm[x]==x:
        return x
    else:
        return find_parent(mm[x])
def get_parent(x):
    if mm[x]==x:
        return x
    else:
        mm[x]=get_parent(mm[x])
        return mm[x]
def union(x,y):
    x=get_parent(x)
    y=get_parent(y)    
    if x!=y:
        mm[y]=x
        
        
n,m = map(int, input().split())
for i in range(n+1):
    mm[i]=i
for _ in range(m):
    try:
        v,a,b=map(int, input().split())
        if not v:
            union(a,b)
        elif find_parent(a)==find_parent(b):
            print("YES") 
        else:
            print("NO")
    except:
        pass