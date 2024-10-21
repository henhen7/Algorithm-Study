def to_minute(time):
    hour, minutes = map(int, time.split(':'))
    return hour * 60 + minutes

s, e, q = map(str, input().split())
start = to_minute(s)
end = to_minute(e)
quit = to_minute(q)

enter = set()
exit = set()
chat = []

record = set()
ans = 0
while True:
    try:
        time_str, name = input().split()
        time_min = to_minute(time_str)

        if time_min <= start:
            record.add(name)
        elif name in record and (end <= time_min <= quit):
            record.remove(name)
            ans += 1
    except:
        break
print(ans)