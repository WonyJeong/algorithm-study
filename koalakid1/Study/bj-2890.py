import sys

input = sys.stdin.readline


if __name__ == "__main__":
    R, C = map(int, input().strip().split())
    graph = [input().strip() for _ in range(R)]
    result = {}
    for line in graph:
        if line.count(".") != C-2:
            count = 0
            while count < C-2:
                point = line[-2 - count]
                if point != ".":
                    if count not in result:
                        result[count] = [int(point)]
                    else:
                        result[count].append(int(point))
                    break
                count += 1
    result = sorted(result.items(), key=lambda x: x[0])
    ranking = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    rank = 1
    for i in result:
        for j in i[1]:
            ranking[j-1] = rank
        rank += 1
    for i in ranking:
        print(i)
