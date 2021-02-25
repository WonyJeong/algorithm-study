#2470
import sys
input = sys.stdin.readline

def solved(N, Lv):
    answer = [sys.maxsize, 0, 0]
    left = 0
    right = N-1
    Lv = sorted(Lv)

    while left < right:
        Sum = Lv[left] + Lv[right]
        if abs(Sum) < abs(answer[0]):
            answer = [Sum, Lv[left], Lv[right]]
            if answer[0] == 0 :
                break
        if Sum < 0 : #음수의 값이 더 크므로 줄여줘야함
            left += 1
        else : #양수의 값이 더 크므로 줄여줘야함
            right -= 1
    return answer[1:]


if __name__ == '__main__':
    N = int(input().strip())
    Lv = list(map(int, input().strip().split()))
    
    for element in solved(N,Lv):
        print(element, end=' ')