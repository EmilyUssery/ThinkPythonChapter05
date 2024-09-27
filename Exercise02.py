#!/usr/bin/env python3

from time import time, mktime

def num_days(epoch_seconds):
    return int(epoch_seconds // 86400)  # 60s * 60m * 24h

def num_hours(epoch_seconds):
    return int(epoch_seconds // 3600)  # 60s * 60m

def num_minutes(epoch_seconds):
    return int(epoch_seconds // 60)  # 60m

def current_time_of_day_naive(epoch_seconds):
    return f"{ (num_hours(epoch_seconds)% 24):02d}:{(num_minutes(epoch_seconds)%60):02d}:{int(epoch_seconds % 60):02d}"

def current_time_of_day(epoch_seconds):
    # 3600 = 60m * 60s and we get hours since epoch, only minutes remain
    hrs_since_epoch, minutes = divmod(epoch_seconds, 3600)
    minutes, seconds = divmod(minutes, 60)  # Now we can get the whole minutes and the remaining seconds.
    # Now we can return the formated current time.
    # Since hours is since epoch, we need the modulus of 24hrs
    # TODO: could handle milli-seconds a bit better, but skipping!
    return f"{int(hrs_since_epoch % 24):02d}:{int(minutes):02d}:{int(seconds):02d}"


time_tuple = (2024, 9, 24, 10, 29, 65, 0, 0, 0)
now = mktime(time_tuple)
#now = time()
print(f"It has been {num_days(now)} days since the Unix epoch!")
print(f"Current epoch time {now} is: {current_time_of_day_naive(now)} GMT")
print(f"Current epoch time {now} is: {current_time_of_day(now)} GMT")