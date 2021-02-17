# +, - 번갈아 출력 (수정용)

print("+, - 번갈아 출력")
n = int(input("n :"))

for _ in range(n//2): #+-를 n//2개 출력
    print('+-',end='')

# for _ in range(1,n//2+1):
#     print('+-',end='')

if n%2 :
    print("+",end='') #n이 홀수일 경우 +를 추가 출력


print()

