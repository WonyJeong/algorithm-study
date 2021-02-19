# *를 n개 출력하되 w개마다 줄바꿈

print("*출력")
n = int(input("n : "))
w = int(input("w : "))

for _ in range(n //w ) : #n//w번 반복
    print('*'*w)

rest = n%w
if rest: 
    print('*'*rest)
