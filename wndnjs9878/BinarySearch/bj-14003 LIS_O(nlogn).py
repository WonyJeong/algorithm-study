#14003
import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution(N, seq):
    lis = [seq[0]]
    res = [0]
    for num in seq[1:]:
        if lis[-1] < num:
            lis.append(num)
            res.append(len(lis)-1)
        else:
            where = bisect_left(lis, num)
            lis[where] = num
            res.append(where)

    length = len(lis)
    print(length)
    ans = []
    for idx in range(len(res)-1, -1, -1):
        if res[idx] == length-1:
            ans.append(seq[idx])
            length -= 1
    
    print(*ans[::-1])


if __name__ == "__main__":
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))
    solution(N, seq)