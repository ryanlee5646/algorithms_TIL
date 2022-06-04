# 주차요금 계산
import collections
import math


def cal_minute(in_time, out_time):
    in_h, in_m = map(int, in_time.split(":"))
    out_h, out_m = map(int, out_time.split(":"))
    minute = (out_h - in_h) * 60 + (out_m - in_m)  # 시간이 -일 경우 고려
    return minute


def cal_fee(basic_minute, basic_fee, unit_minute, unit_fee, record_time):
    result = []
    for i in record_time:
        total_minute = record_time[i]
        total_fee = 5000

        if total_minute < basic_minute:  # 기본시간 보다 적을 경우
            result.append(total_fee)
        else:
            total_fee = int(
                basic_fee
                + (math.ceil((total_minute - basic_minute) / unit_minute)) * unit_fee
            )
            result.append(total_fee)
    return result


# def cal_fee():


def solution(fees, records):
    answer = []
    basic_minute, basic_fee, unit_minute, unit_fee = fees

    check_time = collections.defaultdict(int)
    record_time = collections.defaultdict(int)

    for i in records:
        time, num, in_out = i.split()

        if in_out == "IN":  # IN일 경우 차량 시간 체크
            check_time[num] = time
        else:  # OUT일 경우 시간차이 계산 후 차량 출차
            cal_time = cal_minute(check_time[num], time)
            if record_time[num]:  # 차량이 한번 출입한적 있으면
                record_time[num] += cal_time
            else:  # 차량이 한번도 출입한적 없으면
                record_time[num] = cal_time
            del check_time[num]  # 출차 했으면 차량 지우기

    if check_time:  # 차량이 남아있다면
        for i in check_time:
            cal_time = cal_minute(check_time[i], "23:59")
            if record_time[i]:  # 차량이 한번 출입한적 있으면
                record_time[i] += cal_time
            else:  # 차량이 한번도 출입한적 없으면
                record_time[i] = cal_time
    record_time = dict(sorted(record_time.items()))  # 정렬

    answer = cal_fee(basic_minute, basic_fee, unit_minute, unit_fee, record_time)
    print(answer)
    return answer


# 1
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

# # 2
# fees = [120, 0, 60, 591]
# records = [
#     "16:00 3961 IN",
#     "16:00 0202 IN",
#     "18:00 3961 OUT",
#     "18:00 0202 OUT",
#     "23:58 3961 IN",
# ]

solution(fees, records)
