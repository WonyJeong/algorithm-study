#세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a= int(input('정수 a: ')) #int(문자열) -> 정수화
b= int(input('정수 b: '))
c= int(input('정수 c: '))

max = a
if b> max : max = b
if c> max : max = c

print(f'최대값은 {max}입니다')

#f문자열 포메팅