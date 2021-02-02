#2884
import sys

input = sys.stdin.readline
H,M = map(int, input().strip().split())
if(H!=0):
    if(M>= 45): print(H,(M-45))
    else : print(H-1,M+60-45)
else : 
    if(M>= 45): print(H,(M-45))
    else : print(23,M+60-45)