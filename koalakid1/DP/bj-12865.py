import sys
input = sys.stdin.readline
        
def knapsack():
    global n,k,weight,value
    K = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,k+1):
            if weight[i-1] <= w:
                K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K[n][k])


if __name__ == "__main__":
    n,k = map(int,input().strip().split())
    weight = []
    value = []
    for _ in range(n):
        w,v = map(int,input().strip().split())
        weight.append(w)
        value.append(v)
    knapsack()