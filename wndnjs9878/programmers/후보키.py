import sys
import math
from itertools import combinations
input = sys.stdin.readline

def solution(relation):
    '''
    1. 학생정보 zip
    2. set
    3. set의 수가 relation의 수와 같은지
    4. 같다면 그것은 후보키
    5. 같지 않다면 후보키인것과 하나씩만 묶인채로 후보키가 될 수 있음 
       ==> 단독으로 후보키가 되지 못하는 것들을 조합으로 구하고 그걸 단독 후보키랑 곱해주면됨
    '''
    answer = 0

    allComb = []


    for i in range(1, len(relation[0])+1): #아이템이 몇개나 있는지
        for case in combinations([j for j in range(len(relation[0]))],i):
            allComb.extend([set(case)])

    '''
    유일성 따져야함.
    1. 모든 조합 구해서 만들어놓는다
    ( 이 때, 어차피 다 스트링으로 주어지니까 한번에 합쳐놓는거 어때 )
    '''

    unique = []
    for comb in allComb :
        eachItemComb = set()
        for student in range(len(relation)): # 한 학생
            keystring = ''
            # 한 학생의 정보로만 조합해서 만들어봐
            for item in comb:
                keystring += relation[student][item]
            eachItemComb.add(keystring)
        # print(eachItemComb)
        # print(len(eachItemComb), len(relation))
        if len(eachItemComb) == len(relation): # set의 길이가 row 개수랑 같다면 다 구분된다는 거니까 유일하단거겠지......
            unique.append(comb)

    # print('------------------------')
    # print(unique)

    '''
    최소성 만족해야함.
    유일성 만족하는 것들 - 최소성 위반하는 것들
    최소성 따지려면
    1. Unique안의 원소를 돌면서
    2. 내가 혹시 다른 애들 안에 있나 ? 체크... 
    '''
    violation = set()
    for check in unique:
        for comb in unique:
            if check != comb :
                if comb.issubset(check):
                    violation.add(unique.index(check))

    print(unique)
    print(violation)

    answer = len(unique)-len(violation)
    return answer

if __name__ == "__main__":
    print(solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    ))