def date_to_day(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    today_day = date_to_day(today)
    answer= []
    
    # 유효기간
    terms_dict = {}
    for term in terms:
        type, duration = term.split()
        terms_dict[type] = int(duration)
    
    n = 1
    for privacy in privacies:
        
        date, term = privacy.split()
        apply_day = date_to_day(date)
        delete_day = apply_day + terms_dict[term] * 28 - 1
        
        if today_day > delete_day:
            answer.append(n)
        n += 1
    return answer
