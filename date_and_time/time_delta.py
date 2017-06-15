# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())


import calendar
import datetime

months = list(calendar.month_abbr)

def get_datetime():
    date, day, month, year, time, tz = input().split()
    day = int(day)
    year = int(year)
    month = months.index(month)
    hour, mins, secs = map(int, time.split(':'))
    dt = datetime.datetime(year, month, day, hour, mins, secs)
    
    mins_tz = int(tz) % 100
    hours_tz = int( int(tz) / 100 )
    dt -= datetime.timedelta(  minutes=( mins_tz + hours_tz*60 ) )
    #print( dt )
    return dt
    
def print_delta():
    print( int((get_datetime() - get_datetime()).total_seconds()) ) 
    
for _ in range(n):
    print_delta()
