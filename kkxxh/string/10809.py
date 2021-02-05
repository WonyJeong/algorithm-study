#10809
import sys

input = sys.stdin.readline
S = input().strip()
Arr = []
for i in range(0,123) :
    Arr.append(-1)
for i in range(0,len(S)) :
    if Arr[ord(S[i])] != -1 : continue 
    else : Arr[ord(S[i])] = i

for i in range(97,123) :
    print(Arr[i] ,end=" " )





