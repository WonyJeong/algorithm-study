import sys
from itertools import combinations

input = sys.stdin.readline


def runQuery(q):
    global user
    result = 0
    print("q : ", q)
    for u in user:
        print("u : ", u)
        flag = True
        if u[4] >= q[4]:
            for i in range(4):
                if q[i] == -1:
                    continue
                if q[i] != u[i]:
                    flag = False
                    break
            if flag == True:
                result += 1
    return result


def solution(info, query):
    global user
    answer = []
    category = [
        ["cpp", "java", "python"],
        ["backend", "frontend"],
        ["junior", "senior"],
        ["chicken", "pizza"],
    ]
    user = []
    querys = []
    for info_ in info:
        user_ = info_.split(" ")
        temp = []
        for i in range(4):
            temp.append(category[i].index(user_[i]))
        temp.append(int(user_[4]))
        user.append(temp)
    for q in query:
        q_ = q.split(" and ")
        q = q_[:3] + q_[3].split(" ")
        q[4] = int(q[4])
        temp = []
        for i in range(4):
            if q[i] != "-":
                temp.append(category[i].index(q[i]))
            else:
                temp.append(-1)
        temp.append(int(q[4]))
        querys.append(temp)

    user = sorted(user, key=lambda x: x[4])

    for q in querys:
        answer.append(runQuery(q))

    return answer


if __name__ == "__main__":
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ]
    print(solution(info, query))
