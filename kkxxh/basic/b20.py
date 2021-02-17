#세 정수 최대값

def max3(a,b,c):
    """ a,b,c의 최댓값을 구하여 반환"""
    # """ 여러줄 주석
    maximum = a
    if b > maximum : maximum = b
    if c > maximum : maximum = c
    return maximum #최댓값 반환

print(f'max3(3,2,1) = {max3(3,2,1)}') # a>b>c