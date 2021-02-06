#7568
import sys
input = sys.stdin.readline

def solved(x,y) :
    for i in range(0,len(x)):
        rank = 1
        for j in range(0, len(x)) :
            if x[i] < x[j] and y[i] < y[j] :
                rank += 1
        print(rank)

    return 0

if __name__ == "__main__":
    N = int(input().strip())
    x=[]
    y=[]
    for _ in range(0,N):
        x.append(0)
        y.append(0)
    for i in range(0,N):
        x[i], y[i] = map(int, input().strip().split())
    solved(x,y)