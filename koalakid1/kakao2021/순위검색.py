def dictin(a,d,index):
    if a in d:
        d[a].add(index)
    else:
        d[a] = set()
        d[a].add(index)
    return d

def solution(info, query):
    answer = []
    index = 0
    dic = dict()
    s = []
    ex = set()
    for string in info:
        a,b,c,d,e = string.split()
        dic = dictin(a,dic,index)
        dic = dictin(b,dic,index)
        dic = dictin(c,dic,index)
        dic = dictin(d,dic,index)
        dic = dictin("-",dic,index)
        s.append(int(e))
        index += 1
    
    for string in query:
        string = string.replace("and", "")
        a,b,c,d,e = string.split()
        e = int(e)
        indexes = list(dic[a].intersection(dic[b]).intersection(dic[c]).intersection(dic[d]))
        count = 0
        for i in indexes:
            if s[i] >= e:
                count += 1
        answer.append(count)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])