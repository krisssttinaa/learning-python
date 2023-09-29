import time

#epoch = a date and time from which a computer measures system time
#        when your computer thinks time began (reference point)
print(time.ctime(0)) #convert a time expressed in second since epoch to a readable

print(time.ctime(1000000))

print(time.time()) #return current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_objecttt = time.gmtime()
print(time_objecttt)

time_string = "20 April, 2020"
time_objecttt = time.strptime(time_string, "%d %B, %Y")
print(time_objecttt)

#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) #seconds since epoch
print(time_string)