import math

# record = "time car_num stat"
# time = h, m
# stat = IN / OUT
# fees = [basic_time, basic_fee, unit_time, unit_fee]

# 시간 처리
def time_to_min(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(fees, records):
    parking_time = {}
    in_time = {}
    
    # 입출차
    for record in records:
        time, car_number, status = record.split()
        
        if status == "IN":
            in_time[car_number] = time_to_min(time)
        else:
            parked_time = time_to_min(time) - in_time.pop(car_number)
            parking_time[car_number] = parking_time.get(car_number, 0) + parked_time
    
    # 23:509
    for car_number, time_in in in_time.items():
        parked_time = time_to_min("23:59") - time_in
        parking_time[car_number] = parking_time.get(car_number, 0) + parked_time
    
    def calculate_fee(parked_time):
        basic_time, basic_fee, unit_time, unit_fee = fees
        if parked_time <= basic_time:
            return basic_fee
        else:
            extra_time = parked_time - basic_time
            extra_fee = math.ceil(extra_time / unit_time) * unit_fee
            return basic_fee + extra_fee
    
    answer = []
    for car_number in sorted(parking_time.keys()):
        fee = calculate_fee(parking_time[car_number])
        answer.append(fee)
    
    return answer
