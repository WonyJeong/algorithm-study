'''
내포표기 생성
list 안에서 for, if문을 사용하여 새로운 리스트를 생성하는 기법
'''
numbers = [1,2,3,4,5]
twise = [num*2 for num in numbers if num%2 ==1]
print(twise)