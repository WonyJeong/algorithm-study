#2869
import sys
input = sys.stdin.readline

def solved(A, B, V):
    H = 0 #달팽이가 올라간 높이
    day = 0
    while H < V :
        day += 1  
        H += (A - B)
        if H >= V :
            return day
         




if __name__ == '__main__':
    A, B, V = map(int, input().strip().split())
    print(solved(A,B,V))