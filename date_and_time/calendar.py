month, day, year = map(int, input().split() )
import calendar
print( calendar.day_name[calendar.weekday(year, month, day)].upper() ) 
