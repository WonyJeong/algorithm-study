#1~12까지 8 건너뛰고 출력

for i in range(1, 13):
    if i == 8 :
        continue
    print(i, end=' ')

print()


#list 사용
for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=' ')
print()