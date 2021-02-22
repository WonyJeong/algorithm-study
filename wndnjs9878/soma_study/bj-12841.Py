#12841
import sys
input = sys.stdin.readline

if __name__ == '__main__': 
    N = int(input().strip())
    cross = list(map(int, input().strip().split()))
    left = list(map(int, input().strip().split()))
    right = list(map(int, input().strip().split()))
    dp = [cross[0] for _ in range(N)]

    leftSum = [0 for _ in range(N-1)]
    selected_cross = 1
    
    if N == 1 :
        print(selected_cross, dp[N-1])
        
    else :
        for i in range(N-1):
            cr = dp[i]+right[i]
            leftSum[i] = leftSum[i-1] + left[i]
            lc = leftSum[i] + cross[i+1]
            # print(leftSum)
            if cr <= lc :
                dp [i+1] = cr
            else :
                dp [i+1] = lc
                selected_cross = i + 1
        print(selected_cross+1,dp[N-1])


