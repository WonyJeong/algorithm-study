#2775
import sys

input =sys.stdin.readline

T = int(input())
for i in range(0,T):
    k = int(input())
    n = int(input())

    q = [ i for i in range(1, n+1)]
    for __ in range(k): #?????????????/
        for j in range(1,n):
            q[j] += q[j-1]
    print(q[-1])



    #고침
