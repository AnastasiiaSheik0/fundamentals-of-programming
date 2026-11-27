def time_string(hours, minutes, time_format):
    period = ''
    hour_12 = 0
    result = ''

    if time_format == '12':
        if hours == 0:
            hour_12 = 12
            period = 'am'
        elif hours < 12:
            hour_12 = hours
            period = 'am'
        elif hours == 12:
            hour_12 = 12
            period = 'pm'
        else:
            hour_12 = hours - 12
            period = 'pm'
        result = f"{hour_12}:{minutes:02d}{period}"

    elif time_format == '24':
        result = f"{hours:02d}:{minutes:02d}"

    return result

# Testy z treści zadania:
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
