# 내풀이
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    combins = []
    cols = [i for i in range(col)]
    for i in range(1, col + 1):
        combins.extend(combinations(cols,i))
    
    result = []
    for combin in combins:
        temp = set([tuple(rel[com] for com in combin) for rel in relation])
        if len(temp) == row:
            result.append(combin)
    answer = set(result)
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if len(result[i]) == len(set(result[i]).intersection(set(result[j]))):
                answer.discard(result[j])
                print(answer)
    return len(answer)

#원영 풀이 살짝 고침
import sys
from itertools import combinations

input = sys.stdin.readline


def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    checked = []

    for i in range(1, col + 1):
        for comb in combinations(range(col), i):
            flag = True
            skipThisComb = False
            if checked != []:
                for i in checked:
                    if len(set(i).intersection(set(comb))) == len(i):
                        skipThisComb = True
                        
                        break
            
            if skipThisComb == True:
                continue

            tup = []
            for j in range(0, row):
                temp = []
                for k in range(0, len(comb)):
                    temp.append(relation[j][comb[k]])
                tup.append(tuple(temp))

            tupLen = len(tup)
            tup = set(tup)
            if len(tup) == tupLen:
                answer += 1
                checked.append(comb)

    return answer