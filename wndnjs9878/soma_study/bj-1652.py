#1652
import sys
input = sys.stdin.readline

def transpose(room) :
    transposedList = list(map(list, zip(*room)))
    transposedResult = []
    for i in range(N):
        transposedResult.append(''.join(transposedList[i]))
    return transposedResult

def solution(room):
    garoResult = []
    for row in room :
        garo = '..'  
        firstgaro = row.find(garo)
        if firstgaro != -1 :
            garoResult.append(firstgaro)
        while row[firstgaro+2:].find(garo) != -1:
            temp=row[firstgaro+2:].find(garo) + firstgaro + 2
            if temp-firstgaro!=2:
                firstgaro = temp
                garoResult.append(firstgaro)
            firstgaro = temp
    # print(garoResult)
    return len(garoResult)


if __name__ == '__main__':
    N = int(input().strip())
    room = [input().strip() for _ in range(N)]

    print(solution(room), solution(transpose(room)), sep=' ')
    
    




'''
import sys
input = sys.stdin.readline


def findArea(N, arr):
    answer = 0
    for i in range(N):
        temp = arr[i].split("X")
        for j in range(0, len(temp)):
            if len(temp[j]) >= 2:
                answer += 1

    return answer


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(input().strip())

    transpose = []

    for i in range(N):
        temp = ""
        for j in range(N):
            temp += arr[j][i]
        transpose.append(temp)

    print(findArea(N, arr), findArea(N, transpose))

'''