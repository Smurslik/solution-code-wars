#This kata requires you to convert minutes (int) to hours and minutes in the format hh:mm (string).
#If the input is 0 or negative value, then you should return "00:00"
def time_convert(num):
    if num < 1:
        return "00:00"
    hours = 0
    while num >= 60:
        num -= 60
        hours += 1
    minuts = num % 60
    hours = str(hours)
    minuts = str(minuts)
    if len(hours) < 2:
        hours = "0" + hours
    if len(minuts) < 2:
        minuts = "0" + minuts
    return f'{hours}:{minuts}'
