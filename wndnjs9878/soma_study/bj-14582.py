#14582
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    woolim = list(map(int, input().strip().split()))
    startlink = list(map(int, input().strip().split()))

    woolimScore = 0
    startlinkScore = 0

    while woolimScore < startlinkScore :
        woolimScore += woolim[i]
        startlinkScore += startlink[i]
        print('wS: ', woolimScore)
        print('sS: ',startlinkScore)
        if woolimScore > startlinkScore :
            print("Yes")
            sys.exit(0)
    print("No")