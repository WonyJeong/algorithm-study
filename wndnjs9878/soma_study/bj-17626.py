#17626
# 시간 초과
import sys

if __name__ == '__main__':
    dp = [0,1]
    N = int(input())
    for i in range(2, N+1):
        Min = sys.maxsize
        j = 1
        while (j**2) <= i :
            Min = min(Min, dp[i - (j**2)]) 
            j += 1
        dp.append(Min+1)
    print(dp[N])
