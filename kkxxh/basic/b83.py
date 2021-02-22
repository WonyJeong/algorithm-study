list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(list1 is list2) # False 
# is 는 식별번호의 동일성
list1 = [1,2,3,4,5]
list2 = list1

print(list1 is list2) #True

list1[2] = 9 # 3 -> 9 변경
print(list1)
print(list2)