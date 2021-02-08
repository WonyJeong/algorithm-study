#2108
import sys
input = sys.stdin.readline
from collections import Counter

if __name__ == '__main__':
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(int(input().strip()))

    print( round(sum(arr)/N) ) #산술평균
    arr.sort()
    print( arr[N//2] ) #중앙값
    
    #최빈값
    cnt = Counter(arr).most_common()
    if N != 1 :
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else :
            print(cnt[0][0])
    else :
        print(cnt[0][0])

    print( max(arr) - min(arr) )#범위
    