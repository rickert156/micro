import time

def current_time():
    current_time = time.localtime()

    year = current_time[0]
    month = current_time[1]
    day = current_time[2]
    hour = int(current_time[3])
    minute = current_time[4]
    second = current_time[5]
    
    current_time = f"{day}/{month}/{year} {hour}:{minute}:{second}"
    return current_time

current_time()


