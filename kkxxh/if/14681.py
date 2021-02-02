#14681
import sys

input = sys.stdin.readline
x = int(input().strip())
y = int(input().strip())

if(x > 0):
    if( y> 0) : print("1")
    else : print("4")
else : 
    if (y>0) : print("2")
    else : print("3")