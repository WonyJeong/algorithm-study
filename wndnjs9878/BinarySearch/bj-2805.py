#2805
import sys
input = sys.stdin.readline

def solved(N, M, tree):
    start, end = 1, max(tree)
    answer = 0
    while start <= end:
        mid = (start + end)//2
        forTake = 0 #절단기에 설정할 수 있는 높이
        for i in tree :
            if i-mid >= 0:
                forTake += i - mid
    
        if forTake >= M :
            answer = mid
            start = mid + 1
        else :
            end = mid - 1
    print(answer)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    tree = list(map(int, input().strip().split()))

    solved(N, M, tree)