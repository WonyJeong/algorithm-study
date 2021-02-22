#리스트에서 임의의 원소값을 업데이트

def change(lst,idx,val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val

x = [11,22,33,44,55]
print('x =', x)

index = int(input('index : '))
value = int(input('value : '))

change(x, index, value)
print(f'x = {x}')