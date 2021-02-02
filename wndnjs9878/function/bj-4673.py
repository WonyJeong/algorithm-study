#4673
def noSelfNumber(num) :
    origin = num
    result = origin #생성자 자체를 더하고
    while True :
        result += num%10 #한 자리씩 더한다
        num = int(num/10) #일의자리수부터 상위자리수로 올라가기 위함
        if num == 0 : break #가장 상위자리수가 되었을 때 나눗셈의 결과는 0이 되고 그럼 더이상 더할 필요 없어지므로 빠져나온다
    return result #생성자가 존재하는 수가 리턴됨
        
def numberListInit(numberList) :
    for i in range(0,10001) :
        numberList.append(False)
    return numberList

if __name__ == "__main__" :
    numberList = []
    numberList = numberListInit(numberList)
    for i in range(len(numberList)):
        if noSelfNumber(i) < len(numberList) : numberList[noSelfNumber(i)] = True #생성자가 있는 수는 true로 바꿔줌
        if numberList[i] == False : print(i) #numberList의 false를 가지고 있는 인덱스가 셀프넘버(생성자가 없는 수)가 됨