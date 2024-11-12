# 분 변환
def to_minute(time):
    hour, minutes = map(int, time.split(':'))
    return hour * 60 + minutes

# 샵 변환
def to_char(sheet):
    sheet = sheet.replace("B#", "0")
    sheet = sheet.replace("C#", "1")
    sheet = sheet.replace("D#", "2")
    sheet = sheet.replace("F#", "3")
    sheet = sheet.replace("G#", "4")
    sheet = sheet.replace("A#", "5")
    return sheet

def solution(m, musicinfos):
    m = to_char(m)
    answer = 0
    longest = -9999 
    
    for musicinfo in musicinfos:
        start_time, end_time, title, sheet = musicinfo.split(",")
        # 전처리
        start = to_minute(start_time)
        end = to_minute(end_time)
        play = end - start
        sheet = to_char(sheet)
        
        # 전체 길이
        # 음악 길이 < 재생 시간 = 재생 시간까지 음악 반복
        # 음악 길이 > 재생 시간 = 재생 시간
        etc_play = play % len(sheet)
        total_sheet = (sheet * (play // len(sheet))) + sheet[:etc_play]
        # print(total_sheet)
        
        # 제일 긴거
        if m in total_sheet:
            if play > longest:
                longest = play
                answer = title
    if answer == 0:
        answer = "(None)"
    return answer