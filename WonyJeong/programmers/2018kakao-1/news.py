import sys

input = sys.stdin.readline


def solution(str1, str2):
    answer = 1
    str1 = list(map(str, str1.lower()))
    str2 = list(map(str, str2.lower()))

    dic1 = {}
    dic2 = {}

    for i in range(0, len(str1) - 1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i + 1]) <= 122:
            key = str1[i] + str1[i + 1]
            if not key in dic1.keys():
                dic1[key] = set()
                dic1[key] = 0
            dic1[key] += 1

    for i in range(0, len(str2) - 1):
        if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i + 1]) <= 122:
            key = str2[i] + str2[i + 1]
            if not key in dic2.keys():
                dic2[key] = set()
                dic2[key] = 0
            dic2[key] += 1

    intersection_ = set(dic1.keys()).intersection(set(dic2.keys()))
    union_ = set(dic1.keys()).union(set(dic2.keys()))

    ans1 = 0
    ans2 = 0
    for key in intersection_:
        a = dic1[key]
        b = dic2[key]
        ans1 += min(a, b)

    for key in union_:
        if not key in dic1.keys():
            a = 0
        else:
            a = dic1[key]
        if not key in dic2.keys():
            b = 0
        else:
            b = dic2[key]

        ans2 += max(a, b)

    if ans1 == 0 and ans2 == 0:
        return 65536
    else:
        return int((ans1 / ans2) * 65536.0)


if __name__ == "__main__":
    print(solution("FRANCE", "french"))
