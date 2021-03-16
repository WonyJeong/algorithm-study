import sys
input = sys.stdin.readline
        
def knapsack():
    global n,t
    K = [[0 for _ in range(t+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        k, s = map(int, input().strip().split())
        for j in range(1,t+1):
            K[i][j] = max(s + K[i-1][j-k], K[i-1][j]) if k <= j else K[i-1][j]
    print(K[-1][-1])
if __name__ == "__main__":
    n, t = map(int, input().strip().split())
    time = []
    value = []
    knapsack()