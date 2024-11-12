def solution(record):
    user = {}
    answer = []
    ans = []
    
    for rec in record:
        li = rec.split(' ')
        command = li[0]
        id = li[1]
        
        if command == "Enter" or command == "Change":
            name = li[2]
            user[id] = name
        
        if command == "Enter":
            name = user[id]
            answer.append((id, "님이 들어왔습니다."))
        if command == "Leave":
            answer.append((id, "님이 나갔습니다."))
    for i in range(len(answer)):
        string = str(user[answer[i][0]] + answer[i][1])
        ans.append(string)
    return ans