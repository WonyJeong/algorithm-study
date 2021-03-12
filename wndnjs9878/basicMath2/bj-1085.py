#1085
import sys
input = sys.stdin.readline

def solution(x,y,w,h):
    '''
    1 1 1 1 1 1 1 1 1 1 *
    1 1 1 1 1 1 @       1
    1           1       1
    * 1 1 1 1 1 1 1 1 1 1
    '''

    return min([x , y, w-x, h-y])
        

if __name__ == '__main__':
    x, y, w, h = map(int, input().strip().split())
    print(solution(x, y, w, h))