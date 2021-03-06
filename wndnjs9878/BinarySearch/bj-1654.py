#1654
import sys
input = sys.stdin.readline

def solved(K,N,lan):
    start, end = 1, max(lan)
    answer = 0 #랜선의 길이
    while start <= end :
        mid = (start + end) // 2
        compare = sum([i // mid for i in lan]) #랜선의 개수

        if compare >= N : # 너무 잘게 잘랐네 조금 더 길게 잘라도 되겠다
            answer = mid
            start = mid + 1
        else : # 너무 길게 잘랐어 조금 더 잘게 잘라야되겠다
            end = mid -  1
    print(answer)


if __name__ == '__main__':
    K, N = map(int, input().strip().split())
    lan = [int(input().strip()) for _ in range(K)]
    
    solved(K,N,lan)
