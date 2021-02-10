#26676
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

'''
def DFS(housingComplexArr, cnt, x, y):
    housingComplexArr[x][y] = 0 #들렸다는 표시로 0으로 바꿈
    
    for i in range(4):
        nearX = x + dx[i]
        nearY = y + dy[i]

        if 0 <= nearX < N and 0<= nearY < N:
            if housingComplexArr[nearX][nearY] == 1:
                cnt = DFS(housingComplexArr, cnt+1, nearX, nearY)  
    
    return cnt
'''

def BFS(housingComplexArr, cnt, x, y):
    housingComplexArr[x][y] = 0
    queue = []
    queue.append((x,y))

    while len(queue) > 0 :
        x, y = queue.pop()
        for k in range(4) :
            nearX = x + dx[k]
            nearY = y + dy[k]

            if 0 <= nearX < N and 0<= nearY < N:
                if housingComplexArr[nearX][nearY] == 1:
                    cnt += 1
                    housingComplexArr[nearX][nearY] = 0
                    queue.append((nearX, nearY))
        
    return cnt


if __name__ == '__main__':
    N = int(input().strip())
    housingComplexArr = [ list(map(int, input().strip())) for _ in range(N)]
    numberOFhousesInDangi = [] #answer
    
    for i in range(N):
        for j in range(N):
            if housingComplexArr[i][j] == 1:
                numberOFhousesInDangi.append(BFS(housingComplexArr,1,i,j))


    print(len(numberOFhousesInDangi))
    for element in sorted(numberOFhousesInDangi):
        print(element)
