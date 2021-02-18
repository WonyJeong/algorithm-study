# *를 n개 출력하되 w개마다 줄바꿈

print('*출력')
n = int(input("n : "))
w = int(input("w : "))

for i in range(n) :
    print('*', end='')
    if i % w == w-1 : # n번 판단    
        print() #줄바꿈

if n%w : # n이 w의 배수가 아니면 줄바꿈을 for문 밖에서
    print()