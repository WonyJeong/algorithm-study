#1712
#A만원의 고정비용,  B만원의 가변 비용
#C만원의 노트북 비용
#판매 비용이 고정비용+가변비용보다 많아지는 순간 = 손익분기점

import sys

input=sys.stdin.readline
A, B, C = map(int,input().strip().split())
sell = 0

if C > B :
    sell = int(A / (C-B))
    print(sell+1)
else : print(-1)

    