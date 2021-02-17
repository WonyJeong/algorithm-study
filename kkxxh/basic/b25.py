#세 정수를 입력받아 중앙값 구하기2

def med3(a,b,c):
    """a,b,c의 중앙값을 구하여 반환"""
    if (b >= a and c <= a) or (b <=a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    else : return c

#a,b 비교를 이미 한 상태에서 또 비교하므로 효율적이지 않은 코드