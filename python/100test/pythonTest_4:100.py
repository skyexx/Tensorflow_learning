#Q4
#input year/month/day
#1.Determine whether it is a leap year
#2.Determine the days of each month
#3.for loop to add days that before the input month
#4.add the day

year = int(input('please input a year:'))
# end='' don't move to next line
month = int(input('please input a month:'))
day = int(input('please input a day:'))

if year%4 != 0:
    for month in range(1,month):
        if month == [3,5,7,8,10,12]:
            month = month + 31
        elif month == [4,6,9,11]:
            month = month + 30
        elif month == [2]:
            month = month + 28
        else:
            month = 0
    
else:
    for month in range(1,month):
        if month == [3,5,7,8,10,12]:
            month = month + 31
        elif month == [4,6,9,11]:
            month = month + 30
        elif month == [2]:
            month = month + 29
        else:
            month = 0
number = month + day

print(number)
    

