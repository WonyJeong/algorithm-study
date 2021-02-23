from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().strip().split()))
    b = list(map(int,input().strip().split()))
    b_index = [b.index(a[i]) for i in range(n)]
    
    lis = [b_index[0]]
    for i in b_index[1:]:
        if lis[-1] < i:
            lis.append(i)
        else:
            l = 0
            r = len(lis) - 1
            ret = sys.maxsize
            
            while l <= r:
                mid = (l+r) // 2
                if lis[mid] >= i:
                    if ret > mid:
                        ret = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            lis[ret] = i
    print(len(lis))
