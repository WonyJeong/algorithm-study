#14717
import sys
from itertools import combinations
input = sys.stdin.readline

def solution(A,B):
    card = list(range(1,11)) + list(range(1,11))
    card.remove(A)
    card.remove(B)

    jokbo = list(combinations(card,2))
    

    # 땡으로 이기는 경우
    if A == B :
        answer = (len(jokbo) - (10 - A)) / len(jokbo)
        return '%.3f' %answer


    else:
        win = 0
        for all in jokbo:
            if all[0] == all[1]:
                continue
            elif sum(all)%10 < (A + B) % 10:
                win += 1
        answer = win / len(jokbo)
        return '%.3f' %answer


if __name__ == '__main__':
    A , B = map(int,input().strip().split())
    print(solution(A,B))