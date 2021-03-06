#신규아이디추천
import sys
input = sys.stdin.readline

def solution(new_id):
    #1
    new_id = new_id.lower() 
    #print('1:',new_id)


    #2
    can = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_','.']
    new_id = list(new_id)
    for i in range(len(new_id)):
        if new_id[i] not in can:
            new_id[i] = ''
    new_id = ''.join(new_id)
    #print('2:',new_id)


    #3
    new_id = list(new_id)
    for i in range(len(new_id)-1):
        if new_id[i] == '.' and new_id[i+1] == '.':
            new_id[i] = ''
    new_id = ''.join(new_id)
    #print('3:',new_id)


    #4
    new_id = list(new_id)
    if new_id[0] == '.': 
        new_id[0] = ''
    if new_id[len(new_id)-1] == '.':
        new_id[len(new_id)-1] = ''
    new_id = ''.join(new_id)
    #print('4:',new_id)


    #5
    if new_id == '': 
        new_id = 'a'
    #print('5:',new_id)
    
    
    
    #6
    new_id = list(new_id)
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
        if new_id[len(new_id)-1] == '.':
            new_id[len(new_id)-1] = ''
    #print('6:',new_id)



    #7
    if len(new_id) <= 2:
        while len(new_id) < 3 :
            new_id += new_id[len(new_id)-1]
    new_id = ''.join(new_id)
    #print('7:',new_id)

    return new_id

if __name__ == '__main__':
    new_id = input().strip()
    print(solution(new_id))