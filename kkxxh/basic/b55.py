#오른쪽 아래가 직각인 이등변 삼각형으로 *출력

print('오른쪽 아래가 직각인 이등변 삼각형으로 *출력')
n= int(input('짧은 변의 길이를 입력:'))

for i in range(n):
    for _ in range(n-i-1): 
        print(' ', end='')
    for _ in range(i+1):
        print('*',end='')
    print()