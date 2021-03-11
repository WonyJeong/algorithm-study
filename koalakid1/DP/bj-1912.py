import sys
from bisect import bisect_left

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    l = list(map(int,input().strip().split()))
    count = 0
    temp = []
    for i in range(len(l)):
        if count == 0:
            count += l[i]
        elif count > 0:
            if l[i] >= 0:
                count += l[i]
            else:
                temp.append(count)
                count = l[i]
        else:
            if l[i] <= 0:
                count += l[i]
            else:
                temp.append(count)
                count = l[i]
    if temp == []:
        temp = [count] if count > 0 else l
    d = [0 for _ in range(len(temp))]
    for i in range(len(temp)):
        if i == 0:
            d[i] = temp[i]
        else:
            if d[i-1] >= 0:
                d[i] = max(0,d[i-1] + temp[i])
            else:
                d[i] = max(d[i-1], d[i-1] + temp[i], temp[i])
    print(max(d))