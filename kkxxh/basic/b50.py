#2자리 양수 입력받기

print('2자리 양수 입력')

while True :
    no = int(input('값 입력 : '))
    if no >= 10 and no <= 99 :
        break
print(f'입력받은 양수는 {no}이다')