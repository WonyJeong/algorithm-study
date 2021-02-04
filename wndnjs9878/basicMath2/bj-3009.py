#3009
import sys
input = sys.stdin.readline

def solved(x,y):
    newX = 0
    newY = 0
    for i in range(0,3) :
        if x.count(x[i]) == 1 :
            newX = x[i]
        if y.count(y[i]) == 1 :
            newY = y[i]
    return f'{newX} {newY}'


if __name__=='__main__':
    x = [0,0,0]
    y = [0,0,0]
    for i in range(0,3):
        x[i], y[i] = map (int,input().strip().split())
    print(solved(x,y))