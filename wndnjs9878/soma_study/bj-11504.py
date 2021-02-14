#11504
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        X = input().strip()
        Y = input().strip()

        dolRyeo = list(map(int, input().strip().split()))

        for i in range(M-1):
            dolRyeo.append(dolRyeo[i])

        win = 0
        for i in range(0,N):
            if int(X[0]) <= dolRyeo[i] : 
                    Z = ''
                    for k in range(M):
                        Z += str(dolRyeo[i+k])
                    intZ = int(Z)
                    intX = int(X.replace(' ',''))
                    intY = int(Y.replace(' ',''))
                    if intX <= intZ <= intY:
                        win += 1
        print(win)
