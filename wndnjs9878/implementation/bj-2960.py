#2960 N보다 작거나 같은 모든 소수를 찾는 알고리즘
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    number = [i for i in range(2, N+1)]
    cnt = 0
    while number :
        i = 0
        P = number[i]
        for element in number :
            if element%P == 0 :
                number.remove(element)
                cnt += 1
                if cnt == K :
                    print(element)

        
