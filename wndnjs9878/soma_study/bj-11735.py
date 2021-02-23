#11735
import sys
input = sys.stdin.readline

def solved(square, query):
    answer = []
    for _ in range(len(query)):
        choose, num = query.pop(0)
        if choose == 'R':
            queryresult = 0
            for j in range(N):
                queryresult += square[int(num)-1][j]
                square[int(num)-1][j] = 0
        else :
            queryresult = 0
            for j in range(N):
                queryresult += square[j][int(num)-1]
                square[j][int(num)-1] = 0
        answer.append(queryresult)
    return answer


if __name__ == '__main__':
    N, q = map(int, input().strip().split())
    square = [[i+j for j in range(1,N+1)] for i in range(1,N+1)]
    query = [list(input().strip().split()) for _ in range(q)]
    for element in solved(square, query) :
        print(element)


