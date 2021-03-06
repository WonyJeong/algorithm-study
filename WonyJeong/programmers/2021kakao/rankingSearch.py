import sys
from itertools import combinations
from bisect import bisect_left

input = sys.stdin.readline


def solution(info, query):
    answer = []
    user = {}
    for info_ in info:
        user_ = info_.split(" ")
        user_[4] = int(user_[4])
        for i in range(0, 5):
            for com in combinations(user_[:4], i):
                if not com in user.keys():
                    user[com] = []
                user[com].append(user_[4])

    for key in user.keys():
        user[key] = sorted(user[key])

    for q in query:
        result = 0
        q_ = q.split(" and ")
        q__ = q_[3].split(" ")
        q_ = q_[:3] + q__
        q_[4] = int(q_[4])
        temp = []
        for i in range(4):
            if q_[i] != "-":
                temp.append(q_[i])

        tup = tuple(temp)
        try:
            lowerbound = bisect_left(user[tup], q_[4])
            answer.append(len(user[tup]) - lowerbound)
        except:
            answer.append(0)

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
