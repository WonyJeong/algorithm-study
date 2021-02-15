# import sys

# input = sys.stdin.readline


# def rank(arr, R, C):
#     ranking = [0 for _ in range(9)]
#     for i in range(0, len(arr)):
#         temp = 0
#         for j in range(0, C - 2):
#             if arr[i][C - 2 - j - 1] == ".":
#                 temp += 1
#             else:
#                 ranking[int(arr[i][C - 2 - j - 1]) - 1] = temp

#     dic = {}
#     for i in range(0, 9):
#         if ranking[i] not in dic.keys():
#             dic[ranking[i]] = set()
#         dic[ranking[i]].add(i + 1)

#     newRank = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     cursor = 1

#     sdic = sorted(dic)
#     # print(sdic)
#     for i in range(0, len(sdic)):
#         a = sdic[i]
#         for j in range(0, 9):
#             if ranking[j] == a:
#                 newRank[j] = i + 1

#     print("\n".join(map(str, newRank)))


# if __name__ == "__main__":
#     R, C = map(int, input().strip().split())
#     arr = []
#     temp = "S" + "." * (C - 2) + "F"
#     for _ in range(R):
#         row = input().strip()
#         if row != temp:
#             arr.append(list(row.split("S")[1].split("F")[0]))
#     rank(arr, R, C)


# # 2890 카약
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, input().strip().split())
    contest = []
    ranking = {}
    rankType = []
    for _ in range(R):
        noKayak = "." * (C - 2)
        temp = input().strip()
        if noKayak not in temp:
            contest.append(temp)
            rank = 1›
            for i in range(C - 2, 0, -1):
                if temp[i] == ".":
                    rank += 1
                else:
                    ranking[int(temp[i])] = rank
                    rankType.append(rank)
                    break

    result = sorted(ranking.items(), key=lambda x: x[1])
    rankType = list(set(rankType))

    ssibal = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for re in result:
        idx = list(re)[0]
        numberOfDot = list(re)[1]
        ssibal[idx - 1] = rankType.index(numberOfDot) + 1

    for si in ssibal:
        print(si)


 