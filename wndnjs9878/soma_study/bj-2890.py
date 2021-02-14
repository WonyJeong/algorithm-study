#2890 카약
# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     R, C = map(int, input().strip().split())
#     ranking = {}
#     for _ in range(R):
#         noKayak = '.'*(C-2)
#         temp = input().strip()
#         if noKayak not in temp:
#             rank = 1
#             for i in range(C-2, 0, -1):
#                 if temp[i] == '.':
#                     rank += 1
#                 else : 
#                     ranking[int(temp[i])] = rank
#                     break        
    
#     firstRanking = min(ranking.values())
#     for key, value in ranking.items():
#         if value == firstRanking :
#             ranking[key] = 1


#     result = sorted(ranking.items(), key=lambda x : x[1])
#     kayakRankingSorted = sorted(ranking, key=lambda x : ranking[x])

#     realResult = {}

#     for i in range(0,9):
#         realResult[list(result[i])[0]] = list(result[i])[1]
    
#     for i in range(1,9):
#         if realResult[kayakRankingSorted[i]] != realResult[kayakRankingSorted[i-1]]:
#             ifsameValueExist_Key = realResult[kayakRankingSorted[i]]
#             frontValue = realResult[kayakRankingSorted[i-1]]
#             for key, value in realResult.items():
#                 if value == ifsameValueExist_Key :
#                     realResult[key] = frontValue+1

#     answer = sorted(realResult.items())
#     for i in range(9):
#         print(list(answer[i])[1])


import sys

input = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, input().strip().split())
    ranking = {}
    rankType = []
    for _ in range(R):
        noKayak = "." * (C - 2)
        temp = input().strip()
        if noKayak not in temp:
            rank = 1
            for i in range(C - 2, 0, -1):
                if temp[i] == ".":
                    rank += 1
                else:
                    ranking[int(temp[i])] = rank
                    rankType.append(rank)
                    break

    result = sorted(ranking.items(), key=lambda x: x[1])
    rankType = list(set(rankType))

    # print("ranking : ", ranking)
    # print("result", result)
    # print("rankType : ", rankType)

    kayakRankingInOrder = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for eachRank in result:
        idx = list(eachRank)[0] #카약 번호
        numberOfDot = list(eachRank)[1] #캬악 순위
        kayakRankingInOrder[idx - 1] = rankType.index(numberOfDot) + 1

    for kayak in kayakRankingInOrder:
        print(kayak)