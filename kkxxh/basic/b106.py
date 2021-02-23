
import copy #깊은 복사를 위함

#얕은 복사
x= [[1,2,3],[4,5,6]]
y = x.copy()
x[0][1] = 9
print(x)
print(y)


#깊은 복사
x= [[1,2,3],[4,5,6]]
y = copy.deepcopy(x)
x[0][1] = 9
print(x) #대입된 9 출력
print(y) # y배열에는 영햐을 미치지 않음