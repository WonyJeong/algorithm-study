from bisect import bisect_left
import sys

input = sys.stdin.readline




if __name__ == "__main__":
    n = int(input())
    a = sorted(list(map(int,input().strip().split())))
    
    s = 0
    e = n-1
    answer = [sys.maxsize]
    while s<e:
        temp = a[s] + a[e]
        if abs(temp) < answer[0]:
            answer = [abs(temp), a[s], a[e]]
        if temp == 0:
            break
        if temp > 0:
            e -= 1
        else:
            s += 1
    
    print(*answer[1:])