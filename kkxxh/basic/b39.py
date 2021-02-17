# +, - 번갈아 출력

print("+, - 번갈아 출력")
n = int(input("n :"))

for i in range(n):
    if i % 2 :
        print('-', end='')
    else : print('+', end='')

# for i in range(1,n+1):
#     if i % 2 :
#         print('-', end='')
#     else : print('+', end='')

print()

#for문을 반복할 때마다 if문 수행 -> 문제
