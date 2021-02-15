#2346
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    '''
        5
        3 2 1 -3 -1
    >>> 1 4 5 3 2
    '''

    moveData = list(map(int, input().strip().split()))
    
    idx = 0
    index = [i for i in range(1, N+1)] #풍선 번호
    result = []

    temp = moveData.pop(idx) # 얼만큼 이동해야되는지
    result.append(index.pop(idx)) #풍선 번호를 결과에 저장

    while moveData :
        if temp < 0 :
            idx = (idx + temp) % len(moveData)
        else :
            idx = (idx + (temp-1) ) % len(moveData)
        temp = moveData.pop(idx)
        result.append(index.pop(idx))


    for element in result :
        print(element, end=' ')
    
        
        
