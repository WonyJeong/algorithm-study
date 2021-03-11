import sys
input = sys.stdin.readline
        
def knapsack():
    global n,m,cal,money
    K = [0 for _ in range(m+1)]
    for i in range(n):
        for j in range(1,m+1):
            if money[i] <= j:
                K[j] = max(cal[i] + K[j-money[i]], K[j])
    print(K[-1])
if __name__ == "__main__":
    while True:
        n, m = map(float, input().strip().split())
        n, m = int(n), int(m*100 + 0.5)
        if n == m == 0 :
            break
        money = []
        cal = []
        for _ in range(n):
            c, p = map(float, input().strip().split())
            c, p = int(c), int(p*100 + 0.5)
            cal.append(c)
            money.append(p)
        knapsack()
        
        