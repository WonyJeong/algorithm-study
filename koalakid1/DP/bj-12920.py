import sys
input = sys.stdin.readline
        
def knapsack():
    global n,t
    K = [0 for _ in range(t+1)]
    for i in range(1,n+1):
        v, c, k = map(int, input().strip().split())
        T = 1
        while k > 0:
            temp = min(k, T)
            for j in range(t, temp * v - 1, -1):
                K[j] = max(K[j], temp * c + K[j-v*temp])
            T *= 2
            k -= temp
    print(K[-1])
if __name__ == "__main__":
    n, t = map(int, input().strip().split())
    knapsack()