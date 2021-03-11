#1978
import sys
input = sys.stdin.readline

def solution(N, numbers):
    answer = []
    for num in numbers:
        if num == 1 :
            continue
        if num == 2 :
            answer.append(num)
        for i in range(2,num):
            if num%i == 0:
                break
            elif i == num-1 and num%i != 0 :
                answer.append(num)
            else:
                continue

    return len(answer)

if __name__ == '__main__':
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    print(solution(N, numbers))