#11054 LBS
import sys
input = sys.stdin.readline

def solution(N,seq):
    increase = [1] * N
    decrease = [1] * N
    largest = 0
    for i in range(N):
        for j in range(i):
            if seq[j] < seq[i] :
                increase[i] = max(increase[i], increase[j]+1)
                
    # print(increase)
    seq.reverse()
    for i in range(N):
        for j in range(i):
            if seq[j] < seq[i] :
                decrease[i] = max(decrease[i], decrease[j]+1)

    decrease.reverse()

    result = [0]*N
    for i in range(N):
        result[i] = increase[i] + decrease[i]
    
    return max(result)-1 # -1해주는 이유 : 꺾이는 부분 두 번 더해지므로 


if __name__ == '__main__':
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))   
    print(solution(N,seq))

'''
10
1 5 2 1 4 3 4 5 2 1

1' 5 2' 1 4 3' 4' 5' 2 1
1  2 2  1 3 3  4  5  2 1

reverse()

1' 2' 5 4 3' 4' 1 2 5' 1
1  2  3 3 3  4  1 2 5  1



>> 7

10
10 2 7 6 5 3 2 7 6 2
>> 6
'''