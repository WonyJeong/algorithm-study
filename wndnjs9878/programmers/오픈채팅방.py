
def solution(record):
    answer = []
    state = ['Enter', 'Change', 'Leave']
    userInfo = {}


    for i in range(len(record)) :
        if record[i].split()[0] != state[2]: #Enter or Change
            userInfo[record[i].split()[1]] = record[i].split()[2]

    for i in range(len(record)) :
        if record[i].split()[0] == state[0]: #Enter
            answer.append(f"{userInfo[record[i].split()[1]]}님이 들어왔습니다.")
    
        elif record[i].split()[0] == state[2]: #leave
            answer.append(f"{userInfo[record[i].split()[1]]}님이 나갔습니다.")
        else :
            pass
           
    
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))