#11971
import sys
input = sys.stdin.readline

if __name__ =='__main__':
    N, M = map(int, input().strip().split())
 
    limit = []
    speed = []

    for i in range(N):
        defaultDistance, defaultSpeed = map(int, input().strip().split())
        for j in range(defaultDistance):
            limit.append(defaultSpeed)
    for i in range(M):
        michinDistance, michinSpeed = map(int, input().strip().split())
        for j in range(michinDistance):
            speed.append(michinSpeed)

    answer = 0
    for i in range(100):
        answer = max(answer, speed[i]-limit[i])
    print(answer)
