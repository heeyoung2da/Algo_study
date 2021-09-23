import datetime
a=6
b=24

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = datetime.date(2016, a, b).weekday()
    return days[answer]

solution(a,b)