#4153
import sys
input = sys.stdin.readline

def solved(x,y,z):
    if x**2 == y**2 + z**2 : return 'right'
    elif y**2 == x**2 + z**2 : return 'right'
    elif z**2 == x**2 + y**2 : return 'right'

    return 'wrong'

if __name__=='__main__' :
    while True :
        x,y,z = map(int, input().strip().split())
        if x==0 and y==0 and z==0 :
            break
        print(solved(x,y,z))