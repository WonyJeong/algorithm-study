import sys
from itertools import combinations
from collections import Counter
# 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는데 사용하는 객체
# most_common() : 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
input = sys.stdin.readline

def solution(orders,course):
    '''
    각 손님이 주문한 단품메뉴 조합에 대한 조합을 구한다. (course에 있는 수)
    그 조합들에서 2번 이상 반족되는 것을 코스요리 메뉴 후보에 포함한다.
    '''

    answer = []
    for cnt in course:
        candidates = []
        for menu in orders:
            for comb in combinations(menu,cnt):
                candidates.append(''.join(sorted(comb)))
        #print('candidate',candidates)
        cntOfduplicateCandidates = Counter(candidates).most_common()
        #print('count',cntOfduplicateCandidates)
        answer += [
            menu for menu, count in cntOfduplicateCandidates 
            if count > 1 and count == cntOfduplicateCandidates[0][1]
        ]
    
    return sorted(answer)

if __name__ == '__main__' :
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2,3,5]
    print(solution(orders, course))
