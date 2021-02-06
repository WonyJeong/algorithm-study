#2908
import sys

input = sys.stdin.readline
a, b = map(int,input().strip().split())
a_ = int(str(a)[::-1])
b_ = int(str(b)[::-1])
if a_ > b_ :
    print(a_)
else : print(b_)
