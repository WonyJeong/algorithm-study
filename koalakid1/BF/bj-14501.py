import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    T = []
    P = []

    for i in range(n):
        t,p = map(int,input().strip().split())
        T.append(t)
        P.append(p)

    d = [0 for _ in range(n)]

    d[n-1] = P[n-1] if T[n-1] == 1 else 0
    
    for i in range(n-2, -1,-1):
        day = i + T[i]

        if day == n:
            d[i] = max(P[i], d[i+1])
        elif day < n:
            d[i] = max(P[i] + d[day], d[i+1])
        else:
            d[i] = d[i+1]
    
    print(d[i])


# n = int(input())
# d = []
# p = []
# for i in range(n):
#     a, b = map(int, input().split())
#     d.append(a)
#     p.append(b)

# dp = [0 for i in range(n)]

# if d[n-1] == 1:
#     dp[n-1] = p[n-1]

# for i in range(n-2, -1, -1):
#     day = i + d[i]

#     if day == n:
#         dp[i] = max(p[i], dp[i+1])

#     elif day < n :
#         dp[i] = max(p[i] + dp[day], dp[i+1])

#     elif day > n :
#         dp[i] = dp[i+1]

# print(dp[0])