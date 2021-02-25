#3273
import sys
input = sys.stdin.readline

def solved(N,a,x):
    answer = 0
    left = 0
    right = N-1
    
    a = sorted(a)

    while left < right :
        Sum = a[left] + a[right]
        if Sum == x :
            answer += 1
            left += 1
        elif Sum < x :
            left += 1
        else :
            right -= 1

    return answer

if __name__ == '__main__':
    N = int(input().strip())
    a = list(map(int, input().strip().split() ))
    x = int(input().strip())
    print(solved(N,a,x))
