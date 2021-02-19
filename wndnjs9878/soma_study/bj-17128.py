#17128
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, Q = map(int, input().strip().split())
    quality = list(map(int, input().strip().split()))
    cowNum = list(map(int ,input().strip().split()))
    calculated = [0 for _ in range(N)]
    for i in range(N):
        calculated[i] += (quality[i%N]*quality[(i+1)%N]*quality[(i+2)%N]*quality[(i+3)%N])
    answer = sum(calculated)


    for cow in cowNum:
        for j in range(cow-4, cow):
            calculated[j%N] = calculated[j%N]*(-1)
            answer += 2 * calculated[j%N]
        
        print(answer)
