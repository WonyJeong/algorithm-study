#14582
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    woolim = list(map(int, input().strip().split()))
    startlink = list(map(int, input().strip().split()))

    woolimScore = 0
    startlinkScore = 0

    for i in range(9):
        woolimScore += woolim[i]
        if woolimScore > startlinkScore :
            print("Yes")
            sys.exit(0)
        startlinkScore += startlink[i]
        
    print("No")