import sys
input = sys.stdin.readline

def solution(info, query):
    answer = [0 for _ in range(len(query))]
    dividedInfo = []
    dividedQuery = []
    for sub in query:
        dividedQuery.append(sub.replace(' and','').split(' '))    
    # print(dividedQuery)
    
    for sub in info:
        dividedInfo.append(sub.split(' '))

    # print(dividedInfo)

    '''
    dividedInfo[][-1] : 각 지원자의 코딩테스트 점수
    dividedQuery[][-1] : 개발팀이 원하는 코딩테스트 점수
    '''

    for query in range(len(dividedQuery)): #각 쿼리에 대해서 
        for person in dividedInfo: #지원자 수만큼 포문
            match = 0 # 새로운 지원자의 매칭 조건을 따지기 위한 변수 초기화 
            # 점수는 개발팀이 원하는 점수 이상이기만 하면 됨
            if int(dividedQuery[query][-1]) <= int(person[-1]):
                for i in range(4):
                # print(dividedQuery[query][i], person[i])

                    if dividedQuery[query][i] == '-' :
                        match += 1
                    else :
                        if dividedQuery[query][i] != person[i]:
                            break #매칭되지 않는 요소가 나오면 더 이상 볼 필요 없음 
                        else:
                            match += 1
                    # print(match)

            if match == 4:
                answer[query] += 1
            # print('log>>>',answer[query])

    return answer

if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))