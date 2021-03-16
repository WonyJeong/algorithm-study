import sys
input = sys.stdin.readline
        

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    t = sorted([int(input()) for _ in range(n)])
    left = t[0]
    answer = right = t[-1] * m
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for i in range(n):
            total += mid // t[i]
        if total >= m:
            right = mid - 1
            answer = min(answer,mid)
        else:
            left = mid + 1
    print(answer)